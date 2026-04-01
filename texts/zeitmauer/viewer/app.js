const DATA_URL = "../source/ui-index.json";

const state = {
  data: null,
  activeSection: null,
  activeTerm: null,
  activeThread: null,
  focusHandle: null,
  sectionFilter: "",
  termFilter: "",
  globalSearch: "",
  viewMode: "split",
  loadError: null,
};

const el = {
  datasetStats: document.querySelector("#dataset-stats"),
  globalSearch: document.querySelector("#global-search"),
  jumpResults: document.querySelector("#jump-results"),
  sectionFilter: document.querySelector("#section-filter"),
  termFilter: document.querySelector("#term-filter"),
  modeGerman: document.querySelector("#mode-german"),
  modeSplit: document.querySelector("#mode-split"),
  modeEnglish: document.querySelector("#mode-english"),
  sectionNav: document.querySelector("#section-nav"),
  sectionPanel: document.querySelector("#section-panel"),
  termList: document.querySelector("#term-list"),
  termDetail: document.querySelector("#term-detail"),
  threadList: document.querySelector("#thread-list"),
  threadDetail: document.querySelector("#thread-detail"),
  handleInspector: document.querySelector("#handle-inspector"),
};

document.addEventListener("click", onGlobalClick);
el.globalSearch.addEventListener("input", (event) => {
  state.globalSearch = event.target.value.trim();
  renderJumpResults();
});
el.sectionFilter.addEventListener("input", (event) => {
  state.sectionFilter = event.target.value.trim().toLowerCase();
  renderSectionNav();
});
el.termFilter.addEventListener("input", (event) => {
  state.termFilter = event.target.value.trim().toLowerCase();
  renderTermList();
});
el.modeGerman.addEventListener("click", () => setViewMode("german"));
el.modeSplit.addEventListener("click", () => setViewMode("split"));
el.modeEnglish.addEventListener("click", () => setViewMode("english"));

init();

async function init() {
  try {
    const response = await fetch(DATA_URL);
    if (!response.ok) {
      throw new Error(`Could not load ${DATA_URL} (${response.status})`);
    }
    state.data = await response.json();
    seedState();
    renderAll();
  } catch (error) {
    state.loadError = error;
    renderLoadError();
  }
}

function seedState() {
  const data = state.data;
  state.activeSection = data.sections[0]?.handle ?? null;
  state.activeTerm =
    data.glossary.find((term) => term.handle === "term:schicksalszeit")?.handle ??
    data.glossary[0]?.handle ??
    null;
  state.activeThread = data.threads[0]?.handle ?? null;
  state.focusHandle = state.activeSection;
}

function onGlobalClick(event) {
  const handleButton = event.target.closest("[data-handle]");
  if (handleButton) {
    activateHandle(handleButton.dataset.handle);
    return;
  }

  const jumpButton = event.target.closest("[data-jump-handle]");
  if (jumpButton) {
    activateHandle(jumpButton.dataset.jumpHandle);
    return;
  }
}

function activateHandle(handle) {
  if (!handle || !state.data) {
    return;
  }

  const resolved = resolveHandle(handle);
  state.focusHandle = handle;

  if (!resolved) {
    renderInspector();
    return;
  }

  if (resolved.kind === "section") {
    state.activeSection = handle;
  } else if (resolved.kind === "term") {
    state.activeTerm = handle;
  } else if (resolved.kind === "thread") {
    state.activeThread = handle;
  } else if (resolved.kind === "chunk") {
    state.activeSection = resolved.item.section;
  } else if (resolved.kind === "note") {
    if (resolved.item.section) {
      state.activeSection = resolved.item.section;
    }
  } else if (resolved.kind === "evidence") {
    state.activeTerm = resolved.item.term;
    state.activeSection = sectionHandleFromAnchor(resolved.item.anchor);
  }

  renderAll();
}

function renderAll() {
  renderDatasetStats();
  renderModeButtons();
  renderJumpResults();
  renderSectionNav();
  renderSectionDetail();
  renderTermList();
  renderTermDetail();
  renderThreadList();
  renderThreadDetail();
  renderInspector();
}

function renderLoadError() {
  const message = escapeHtml(state.loadError?.message ?? "Unknown error");
  const detail =
    window.location.protocol === "file:"
      ? "Open the repo through a local server, for example `python3 -m http.server` from the repo root, then visit `/texts/zeitmauer/viewer/`."
      : "Check that `texts/zeitmauer/source/ui-index.json` exists and can be fetched.";

  const errorMarkup = `
    <div class="error-state">
      <p><strong>Viewer failed to load.</strong></p>
      <p>${message}</p>
      <p>${escapeHtml(detail)}</p>
    </div>
  `;

  el.sectionPanel.innerHTML = errorMarkup;
  el.sectionNav.innerHTML = errorMarkup;
  el.termList.innerHTML = errorMarkup;
  el.termDetail.innerHTML = "";
  el.threadList.innerHTML = "";
  el.threadDetail.innerHTML = "";
  el.handleInspector.innerHTML = "";
}

function renderDatasetStats() {
  const counts = state.data.counts;
  const items = [
    ["sections", counts.sections],
    ["terms", counts.terms],
    ["evidence", counts.evidence],
    ["threads", counts.threads],
    ["relations", counts.relations],
  ];

  el.datasetStats.innerHTML = items
    .map(
      ([label, value]) =>
        `<span class="stat-pill"><strong>${value}</strong> ${escapeHtml(label)}</span>`,
    )
    .join("");
}

function renderModeButtons() {
  el.modeGerman.classList.toggle("is-active", state.viewMode === "german");
  el.modeSplit.classList.toggle("is-active", state.viewMode === "split");
  el.modeEnglish.classList.toggle("is-active", state.viewMode === "english");
}

function setViewMode(mode) {
  state.viewMode = mode;
  renderSectionDetail();
  renderModeButtons();
}

function renderJumpResults() {
  const query = state.globalSearch.toLowerCase();
  if (!query) {
    el.jumpResults.innerHTML = "";
    return;
  }

  const results = buildSearchIndex()
    .filter((item) => item.searchText.includes(query))
    .slice(0, 8);

  if (!results.length) {
    el.jumpResults.innerHTML = `<div class="empty-state">No matching handles or labels yet.</div>`;
    return;
  }

  el.jumpResults.innerHTML = results
    .map(
      (item) => `
        <button class="jump-item" type="button" data-jump-handle="${escapeAttr(item.handle)}">
          <strong>${escapeHtml(item.label)}</strong>
          <small>${escapeHtml(item.kind)} · ${escapeHtml(item.handle)}</small>
        </button>
      `,
    )
    .join("");
}

function buildSearchIndex() {
  const sectionItems = state.data.sections.map((section) => ({
    handle: section.handle,
    kind: "section",
    label: `${section.label} ${section.part_title_en}`,
    searchText: `${section.handle} ${section.label} ${section.part_title_de} ${section.part_title_en} ${section.de} ${section.en}`.toLowerCase(),
  }));

  const termItems = state.data.glossary.map((term) => ({
    handle: term.handle,
    kind: "term",
    label: `${term.term} -> ${term.preferred ?? "open"}`,
    searchText: `${term.handle} ${term.term} ${term.preferred ?? ""} ${(term.alternatives ?? []).join(" ")} ${term.notes ?? ""}`.toLowerCase(),
  }));

  const threadItems = state.data.threads.map((thread) => ({
    handle: thread.handle,
    kind: "thread",
    label: thread.title ?? thread.handle,
    searchText: `${thread.handle} ${thread.title ?? ""} ${thread.note ?? ""} ${thread.content ?? ""}`.toLowerCase(),
  }));

  const chunkItems = state.data.chunks.map((chunk) => ({
    handle: chunk.handle,
    kind: "chunk",
    label: chunk.handle,
    searchText: `${chunk.handle} ${chunk.note ?? ""}`.toLowerCase(),
  }));

  const noteItems = state.data.notes.map((note) => ({
    handle: note.handle,
    kind: "note",
    label: note.heading ?? note.handle,
    searchText: `${note.handle} ${note.heading ?? ""} ${note.note ?? ""}`.toLowerCase(),
  }));

  return [...sectionItems, ...termItems, ...threadItems, ...chunkItems, ...noteItems];
}

function renderSectionNav() {
  const groups = state.data.sections.reduce((acc, section) => {
    if (!matchesSectionFilter(section)) {
      return acc;
    }
    const key = section.part_slug;
    if (!acc[key]) {
      acc[key] = [];
    }
    acc[key].push(section);
    return acc;
  }, {});

  const markup = Object.entries(groups)
    .map(([partSlug, sections]) => {
      const sample = sections[0];
      return `
        <section class="part-group">
          <div class="part-heading">
            <strong>${escapeHtml(sample.part_title_en)}</strong>
            <small>${escapeHtml(sample.part_title_de)} · ${escapeHtml(partSlug)}</small>
          </div>
          <div class="section-links">
            ${sections.map(renderSectionLink).join("")}
          </div>
        </section>
      `;
    })
    .join("");

  el.sectionNav.innerHTML = markup || `<div class="empty-state">No sections match the current filter.</div>`;
}

function renderSectionLink(section) {
  const isActive = section.handle === state.activeSection;
  return `
    <button
      class="section-link ${isActive ? "is-active" : ""}"
      type="button"
      data-handle="${escapeAttr(section.handle)}"
    >
      <strong>${escapeHtml(section.label)} · ${escapeHtml(section.handle)}</strong>
      <small>${escapeHtml(section.part_title_en)}</small>
    </button>
  `;
}

function matchesSectionFilter(section) {
  if (!state.sectionFilter) {
    return true;
  }
  const haystack = `${section.handle} ${section.label} ${section.part_title_de} ${section.part_title_en}`.toLowerCase();
  return haystack.includes(state.sectionFilter);
}

function renderSectionDetail() {
  const section = resolveHandle(state.activeSection)?.item;
  if (!section) {
    el.sectionPanel.innerHTML = `<div class="empty-state">Select a section to begin.</div>`;
    return;
  }

  const sectionChunks = state.data.chunks.filter((chunk) => chunk.section === section.handle);
  const sectionNotes = state.data.notes.filter((note) => note.section === section.handle);
  const sectionEvidence = state.data.evidence.filter(
    (evidence) => sectionHandleFromAnchor(evidence.anchor) === section.handle,
  );

  const sectionHandles = new Set([
    section.handle,
    ...sectionChunks.map((chunk) => chunk.handle),
    ...sectionNotes.map((note) => note.handle),
  ]);

  const sectionRelations = state.data.relations.filter(
    (relation) =>
      sectionHandles.has(relation.from) ||
      sectionHandles.has(relation.to) ||
      sectionHandleFromAnchor(relation.from) === section.handle ||
      sectionHandleFromAnchor(relation.to) === section.handle,
  );
  const sectionThreads = collectSectionThreads(sectionRelations);

  el.sectionPanel.innerHTML = `
    <header class="section-header">
      <div class="section-title-row">
        <div>
          <p class="eyebrow">${escapeHtml(section.part_title_en)}</p>
          <h2>${escapeHtml(section.label)} · ${escapeHtml(section.handle)}</h2>
        </div>
        <div class="handle-row">
          ${handleButton(section.handle, { active: state.focusHandle === section.handle })}
          <span class="status-pill">${escapeHtml(section.part_title_de)}</span>
        </div>
      </div>
      <div class="meta-row">
        <div class="meta-card">
          <strong>German source</strong>
          <div class="artifact-meta">${escapeHtml(section.source_file)}</div>
        </div>
        <div class="meta-card">
          <strong>Draft source</strong>
          <div class="artifact-meta">${escapeHtml(section.draft_file)}</div>
        </div>
      </div>
    </header>

    ${renderSectionCommentary(sectionThreads)}

    ${renderParallelText(section)}

    <section class="support-grid">
      ${renderArtifactBlock("Named Chunks", sectionChunks, renderChunkCard, "No named chunks yet.")}
      ${renderArtifactBlock("Notes", sectionNotes, renderNoteCard, "No section notes attached.")}
      ${renderArtifactBlock(
        "Evidence Anchored Here",
        sectionEvidence,
        renderEvidenceCard,
        "No glossary evidence items land here yet.",
      )}
      ${renderArtifactBlock(
        "Relations",
        sectionRelations,
        renderRelationCard,
        "No relations touch this section yet.",
      )}
    </section>
  `;
}

function renderSectionCommentary(threads) {
  if (!threads.length) {
    return `
      <section class="section-commentary detail-block">
        <h3>Commentary Threads</h3>
        <div class="empty-state">No commentary threads touch this section directly yet.</div>
      </section>
    `;
  }

  return `
    <section class="section-commentary detail-block">
      <h3>Commentary Threads</h3>
      <div class="artifact-list">
        ${threads.map(renderThreadTouchpointCard).join("")}
      </div>
    </section>
  `;
}

function renderParallelText(section) {
  const deParagraphs = section.de_paragraphs ?? splitParagraphs(section.de);
  const enParagraphs = section.en_paragraphs ?? splitParagraphs(section.en);
  const alignment = section.paragraph_alignment ?? {
    de_count: deParagraphs.length,
    en_count: enParagraphs.length,
    aligned: deParagraphs.length === enParagraphs.length,
    row_count: Math.max(deParagraphs.length, enParagraphs.length),
  };
  const languages = [
    state.viewMode !== "english"
      ? { key: "de", label: "German Source", paragraphs: deParagraphs }
      : null,
    state.viewMode !== "german"
      ? { key: "en", label: "English Draft", paragraphs: enParagraphs }
      : null,
  ].filter(Boolean);

  const columnCount = languages.length || 1;
  const rows = Array.from({ length: alignment.row_count }, (_, index) => {
    return languages
      .map((language) => renderParagraphCell(language, index))
      .join("");
  }).join("");

  return `
    <section class="parallel-text">
      <div class="parallel-head columns-${columnCount}">
        ${languages
          .map(
            (language) => `
              <div class="parallel-column-head">
                <strong>${escapeHtml(language.label)}</strong>
                <small>${language.paragraphs.length} paragraphs</small>
              </div>
            `,
          )
          .join("")}
      </div>
      ${
        alignment.aligned
          ? ""
          : `
            <div class="alignment-warning">
              Paragraph counts diverge here: German ${alignment.de_count}, English ${alignment.en_count}.
              The viewer is pairing by row and leaving any missing side blank.
            </div>
          `
      }
      <div class="parallel-grid columns-${columnCount}">
        ${rows}
      </div>
    </section>
  `;
}

function renderParagraphCell(language, index) {
  const paragraph = language.paragraphs[index];
  const empty = !paragraph;
  return `
    <article class="parallel-cell language-${escapeAttr(language.key)} ${empty ? "is-empty" : ""}">
      <div class="parallel-index">p${index + 1}</div>
      ${
        empty
          ? `<p class="parallel-body parallel-empty">No corresponding paragraph.</p>`
          : `<p class="parallel-body">${escapeHtml(paragraph)}</p>`
      }
    </article>
  `;
}

function renderArtifactBlock(title, items, renderer, emptyMessage) {
  if (!items.length) {
    return `
      <section class="detail-block">
        <h3>${escapeHtml(title)}</h3>
        <div class="empty-state">${escapeHtml(emptyMessage)}</div>
      </section>
    `;
  }

  return `
    <section class="detail-block">
      <h3>${escapeHtml(title)}</h3>
      <div class="artifact-list">
        ${items.map(renderer).join("")}
      </div>
    </section>
  `;
}

function renderChunkCard(chunk) {
  return `
    <article class="artifact-card ${state.focusHandle === chunk.handle ? "is-focus" : ""}">
      <div class="handle-row">
        ${handleButton(chunk.handle, { active: state.focusHandle === chunk.handle })}
      </div>
      <p>${escapeHtml(chunk.note ?? "")}</p>
      <div class="artifact-meta">${escapeHtml(chunk.file ?? "")}</div>
    </article>
  `;
}

function renderNoteCard(note) {
  return `
    <article class="artifact-card ${state.focusHandle === note.handle ? "is-focus" : ""}">
      <div class="handle-row">
        ${handleButton(note.handle, { active: state.focusHandle === note.handle })}
      </div>
      <p>${escapeHtml(note.note ?? "")}</p>
      <div class="artifact-meta">${escapeHtml(note.kind ?? "note")} · ${escapeHtml(note.file ?? "")}</div>
    </article>
  `;
}

function renderEvidenceCard(evidence) {
  return `
    <article class="artifact-card ${state.focusHandle === evidence.handle ? "is-focus" : ""}">
      <div class="handle-row">
        ${handleButton(evidence.handle, { active: state.focusHandle === evidence.handle })}
        ${handleButton(evidence.term)}
      </div>
      <p>${escapeHtml(evidence.note ?? "")}</p>
      <div class="artifact-meta">${escapeHtml(evidence.relation ?? "grounds")} · ${escapeHtml(evidence.anchor)}</div>
    </article>
  `;
}

function renderRelationCard(relation) {
  return `
    <article class="artifact-card">
      <div class="relation-line">
        ${handleButton(relation.from)} <small>${escapeHtml(relation.relation)}</small> ${handleButton(relation.to)}
      </div>
      <p>${escapeHtml(relation.note ?? "")}</p>
    </article>
  `;
}

function collectSectionThreads(relations) {
  const grouped = new Map();

  for (const relation of relations) {
    for (const handle of [relation.from, relation.to]) {
      const resolved = resolveHandle(handle);
      if (resolved?.kind !== "thread") {
        continue;
      }

      const existing = grouped.get(handle) ?? {
        thread: resolved.item,
        touches: [],
      };

      existing.touches.push({
        from: relation.from,
        to: relation.to,
        relation: relation.relation,
        note: relation.note,
      });

      grouped.set(handle, existing);
    }
  }

  return Array.from(grouped.values());
}

function renderThreadTouchpointCard(entry) {
  const { thread, touches } = entry;
  const touchMarkup = touches.length
    ? `
      <div class="thread-touch-list">
        ${touches
          .map(
            (touch) => `
              <div class="thread-touch">
                <div class="relation-line">
                  ${handleButton(touch.from)} <small>${escapeHtml(touch.relation)}</small> ${handleButton(touch.to)}
                </div>
                <p>${escapeHtml(touch.note ?? "")}</p>
              </div>
            `,
          )
          .join("")}
      </div>
    `
    : "";

  return `
    <article class="artifact-card ${state.focusHandle === thread.handle ? "is-focus" : ""}">
      <div class="handle-row">
        ${handleButton(thread.handle, { active: state.focusHandle === thread.handle })}
        <span class="status-pill status-${escapeAttr(thread.status)}">${escapeHtml(thread.status)}</span>
      </div>
      <h3>${escapeHtml(thread.title ?? thread.handle)}</h3>
      <p>${escapeHtml(thread.note ?? "")}</p>
      ${touchMarkup}
      <div class="artifact-meta">${escapeHtml(thread.file ?? "")}</div>
    </article>
  `;
}

function renderTermList() {
  const terms = state.data.glossary.filter((term) => matchesTermFilter(term));
  if (!terms.length) {
    el.termList.innerHTML = `<div class="empty-state">No glossary entries match the current filter.</div>`;
    return;
  }

  el.termList.innerHTML = terms
    .map(
      (term) => `
        <button
          class="term-row ${term.handle === state.activeTerm ? "is-active" : ""}"
          type="button"
          data-handle="${escapeAttr(term.handle)}"
        >
          <strong>${escapeHtml(term.term)}</strong>
          <small>${escapeHtml(term.preferred ?? "open")} · ${escapeHtml(term.status)}</small>
        </button>
      `,
    )
    .join("");
}

function renderTermDetail() {
  const term = resolveHandle(state.activeTerm)?.item;
  if (!term) {
    el.termDetail.innerHTML = `<div class="empty-state">Select a term to inspect its evidence chain.</div>`;
    return;
  }

  const evidence = term.evidence
    .map((handle) => resolveHandle(handle)?.item)
    .filter(Boolean);

  el.termDetail.innerHTML = `
    <section class="detail-block">
      <div class="handle-row">
        ${handleButton(term.handle, { active: state.focusHandle === term.handle })}
        <span class="status-pill status-${escapeAttr(term.status)}">${escapeHtml(term.status)}</span>
      </div>
      <h3>${escapeHtml(term.term)}</h3>
      <p>${escapeHtml(term.notes ?? "")}</p>
      <div class="artifact-meta">Preferred: ${escapeHtml(term.preferred ?? "open")}</div>
      ${
        term.alternatives?.length
          ? `<div class="handle-burst">${term.alternatives
              .map((alt) => `<span class="term-chip">${escapeHtml(alt)}</span>`)
              .join("")}</div>`
          : ""
      }
    </section>
    <section class="detail-block">
      <h3>Evidence Chain</h3>
      ${
        evidence.length
          ? evidence.map(renderEvidenceCard).join("")
          : `<div class="empty-state">This term does not have structured evidence yet.</div>`
      }
    </section>
  `;
}

function matchesTermFilter(term) {
  if (!state.termFilter) {
    return true;
  }
  const haystack = `${term.handle} ${term.term} ${term.preferred ?? ""} ${(term.alternatives ?? []).join(" ")} ${term.notes ?? ""}`.toLowerCase();
  return haystack.includes(state.termFilter);
}

function renderThreadList() {
  const threads = state.data.threads;
  if (!threads.length) {
    el.threadList.innerHTML = `<div class="empty-state">No threads are indexed yet.</div>`;
    return;
  }

  el.threadList.innerHTML = threads
    .map(
      (thread) => `
        <button
          class="thread-row ${thread.handle === state.activeThread ? "is-active" : ""}"
          type="button"
          data-handle="${escapeAttr(thread.handle)}"
        >
          <strong>${escapeHtml(thread.title ?? thread.handle)}</strong>
          <small>${escapeHtml(thread.status)} · ${escapeHtml(thread.note ?? "")}</small>
        </button>
      `,
    )
    .join("");
}

function renderThreadDetail() {
  const thread = resolveHandle(state.activeThread)?.item;
  if (!thread) {
    el.threadDetail.innerHTML = `<div class="empty-state">Select a thread to traverse it.</div>`;
    return;
  }

  const relatedRelations = state.data.relations.filter(
    (relation) => relation.from === thread.handle || relation.to === thread.handle,
  );

  const traversalMarkup = renderThreadDocument(thread);

  el.threadDetail.innerHTML = `
    <section class="thread-card ${state.focusHandle === thread.handle ? "is-focus" : ""}">
      <div class="handle-row">
        ${handleButton(thread.handle, { active: state.focusHandle === thread.handle })}
        <span class="status-pill status-${escapeAttr(thread.status)}">${escapeHtml(thread.status)}</span>
      </div>
      <h3>${escapeHtml(thread.title ?? thread.handle)}</h3>
      <p>${escapeHtml(thread.note ?? "")}</p>
      <div class="thread-file">${escapeHtml(thread.file ?? "")}</div>
    </section>

    <section class="detail-block">
      <h3>Thread Relations</h3>
      ${
        relatedRelations.length
          ? relatedRelations.map(renderRelationCard).join("")
          : `<div class="empty-state">No explicit thread relations yet.</div>`
      }
    </section>

    <section class="detail-block">
      <h3>Traversal Note</h3>
      ${traversalMarkup}
    </section>
  `;
}

function renderThreadDocument(thread) {
  if (!thread?.content) {
    return `<div class="empty-state">No thread dossier content has been exported yet.</div>`;
  }
  return renderThreadMarkdown(thread.content);
}

function renderThreadMarkdown(markdown) {
  const lines = markdown.split(/\r?\n/);
  const blocks = [];
  let index = 0;

  while (index < lines.length) {
    const line = lines[index];

    if (!line.trim()) {
      index += 1;
      continue;
    }

    if (line.startsWith("# ")) {
      blocks.push(`<h4>${formatInline(line.replace(/^# /, ""))}</h4>`);
      index += 1;
      continue;
    }

    if (line.startsWith("## ")) {
      blocks.push(`<h4>${formatInline(line.replace(/^## /, ""))}</h4>`);
      index += 1;
      continue;
    }

    if (line.startsWith("- ")) {
      const items = [];
      while (index < lines.length && lines[index].startsWith("- ")) {
        items.push(`<li>${formatInline(lines[index].slice(2))}</li>`);
        index += 1;
      }
      blocks.push(`<ul>${items.join("")}</ul>`);
      continue;
    }

    const paragraph = [];
    while (index < lines.length && lines[index].trim() && !/^(#|- )/.test(lines[index])) {
      paragraph.push(lines[index]);
      index += 1;
    }
    blocks.push(`<p>${formatInline(paragraph.join(" "))}</p>`);
  }

  const handles = uniqueHandles(markdown);
  const handleBurst = handles.length
    ? `<div class="handle-burst">${handles.map((handle) => handleButton(handle)).join("")}</div>`
    : "";

  return `<div class="thread-markdown">${handleBurst}${blocks.join("")}</div>`;
}

function renderInspector() {
  const resolved = resolveHandle(state.focusHandle ?? state.activeSection);
  if (!resolved) {
    el.handleInspector.innerHTML = `<div class="empty-state">Select any handle to inspect it.</div>`;
    return;
  }

  const { kind, item } = resolved;
  const description = describeResolvedHandle(resolved);

  el.handleInspector.innerHTML = `
    <section class="inspector-card">
      <div class="handle-row">
        ${handleButton(item.handle, { active: true })}
        <span class="status-pill">${escapeHtml(kind)}</span>
      </div>
      <h3>${escapeHtml(description.title)}</h3>
      <p>${escapeHtml(description.body)}</p>
      <div class="artifact-meta">${escapeHtml(description.meta)}</div>
    </section>
  `;
}

function describeResolvedHandle(resolved) {
  const { kind, item } = resolved;

  if (kind === "section") {
    return {
      title: `${item.label} in ${item.part_title_en}`,
      body: firstSentence(item.en),
      meta: `${item.source_file} | ${item.draft_file}`,
    };
  }

  if (kind === "term") {
    return {
      title: item.term,
      body: item.notes ?? "No notes attached.",
      meta: `${item.status} | preferred: ${item.preferred ?? "open"}`,
    };
  }

  if (kind === "chunk") {
    return {
      title: item.handle,
      body: item.note ?? "No chunk note attached.",
      meta: item.file ?? "No file path",
    };
  }

  if (kind === "note") {
    return {
      title: item.heading ?? item.handle,
      body: item.note ?? "No note body attached.",
      meta: `${item.kind ?? "note"} | ${item.file ?? "No file path"}`,
    };
  }

  if (kind === "thread") {
    return {
      title: item.title ?? item.handle,
      body: item.note ?? "No thread summary attached.",
      meta: `${item.status} | ${item.file ?? "No file path"}`,
    };
  }

  if (kind === "evidence") {
    return {
      title: item.handle,
      body: item.note ?? "No evidence note attached.",
      meta: `${item.term} -> ${item.anchor}`,
    };
  }

  return {
    title: item.handle ?? "Unknown handle",
    body: "No description available.",
    meta: kind,
  };
}

function resolveHandle(handle) {
  if (!handle || !state.data) {
    return null;
  }

  const reference = state.data.indexes.by_handle[handle];
  if (!reference) {
    return null;
  }

  const sourceMap = {
    section: state.data.sections,
    term: state.data.glossary,
    chunk: state.data.chunks,
    note: state.data.notes,
    thread: state.data.threads,
    evidence: state.data.evidence,
  };

  const item = sourceMap[reference.kind]?.[reference.index];
  if (!item) {
    return null;
  }

  return { kind: reference.kind, item };
}

function handleButton(handle, options = {}) {
  const active = options.active ? "is-focus" : "";
  return `
    <button
      class="handle-chip ${active}"
      type="button"
      data-handle="${escapeAttr(handle)}"
    >
      ${escapeHtml(handle)}
    </button>
  `;
}

function splitParagraphs(text) {
  return text
    .split(/\n\s*\n/g)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean);
}

function sectionHandleFromAnchor(anchor) {
  const match = String(anchor).match(/^([a-z]+:\d+)/);
  return match ? match[1] : String(anchor);
}

function uniqueHandles(markdown) {
  const found = [];
  const seen = new Set();
  const regex = /`([^`\n]+:[^`\n]+)`/g;
  let match;

  while ((match = regex.exec(markdown))) {
    const handle = match[1];
    if (!seen.has(handle)) {
      seen.add(handle);
      found.push(handle);
    }
  }

  return found;
}

function formatInline(text) {
  const parts = [];
  const regex = /`([^`\n]+)`/g;
  let lastIndex = 0;
  let match;

  while ((match = regex.exec(text))) {
    parts.push(escapeHtml(text.slice(lastIndex, match.index)));
    const token = match[1];
    if (resolveHandle(token)) {
      parts.push(handleButton(token));
    } else {
      parts.push(`<code>${escapeHtml(token)}</code>`);
    }
    lastIndex = regex.lastIndex;
  }

  parts.push(escapeHtml(text.slice(lastIndex)));
  return parts.join("");
}

function firstSentence(text) {
  const sentence = splitParagraphs(text)[0] ?? "";
  return sentence.length > 210 ? `${sentence.slice(0, 207)}...` : sentence;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function escapeAttr(value) {
  return escapeHtml(value);
}
