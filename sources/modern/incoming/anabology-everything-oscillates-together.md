---
title: "Everything Oscillates Together"
author: "anabology"
site: "Substack"
published: 2026-04-06T00:00:00+00:00
source: "https://anabology.substack.com/p/everything-oscillates-together"
domain: "substack.com"
language: "en"
description: "(in yeast)"
word_count: 2180
encounter_status: located
reason: "Pressure on term:substanzbegriff / term:funktionsbegriff. Michaelis-Menten → Yang-Ling as substance-to-function transition. Good neighbor for Erkenntnisproblem when it reaches the relevant chapters."
---

In my [previous post](https://substack.com/home/post/p-192474951) I stated:

" **Biophysics offers global variables that determine what a cell is and how it feels.**"

This is a big claim and will take a lot of time to unravel but I want to quickly share some evidence that makes me excited.

But first - in developing this idea, I've put together a few axioms. Put simply:

1. **Generic Coupling**: biophysical variables are all coupled, save very few exceptions.
2. **Biophysical Sufficiency**: you can control what a cell is / does by controlling biophysical variables
3. **Tissue Coherence**: cells in a group share biophysics; cells that are isolated do not.

These axioms paint a picture where there aren't actually that many cell states, and you can control just about everything about a cell just by nudging it biophysically.

Digging through some old papers I'd saved, I re-discovered a series of studies that touch on all three axioms - in yeast.

**Yeast papers: insanity**

These papers are an attempt to explain a peculiar phenomenon in baker's yeast: if you starve them of glucose and then pack them together into a dense pellet, the metabolic rate of every yeast starts to oscillate synchronously on ~minute-long timescales.

The metabolic oscillations look like this:

*Glycolytic oscillations in yeast - stopped by IAA poisoning of ATP.*

Naturally, metabolic oscillations are oscillations in ATP -- that's what metabolism produces. The ATP oscillations have been confirmed and replicated by many groups.

Luis Bagatolli's group stepped into the arena and measured many more biophysical variables than just 'ATP,' such as water structure, redox state, K+ concentration, etc.

Bagatolli had a fresh perspective and was about to flip the field on its head. You see, he was a long-term supporter of Gilbert Ling's Association-Induction Hypothesis, a theory of the cell in which ATP binds to proteins and alters both the structure of water around them and their binding preference towards potassium.

**In short: Ling said water structure matters.** **A lot.**

This is a non-mainstream model of bioelectricity that was sidelined decades ago - unfairly, in my opinion - but more on that in future posts.

With Ling's model in mind, where water structure, K+, and ATP are proposed to be coupled, the natural question to ask when seeing metabolism oscillate is: "are the water structure and K+ oscillating as well?"

Bagatolli asked this question and Ling was vindicated:

*NADH autofluorescence = redox state, ACDAN GP = water structure. K+ oscillations were demonstrated in a later paper via PBFI measurement.*

**The ATP oscillations were exactly in phase with oscillations of K+, redox state, and water structure.**

Okay -- but of course they are! This doesn't need a new fringe theory. It's just basic biochemistry! The sodium pump should change its rate depending on ATP concentration, metabolism is driven by redox state... and water...

There isn't a good explanation for water.

**So the next step is to see: what can we do with water?**

This is the exciting part:

Bagatolli's group used a fluorescent probe called ACDAN that reports on something called "dipolar relaxation," basically, how freely water molecules can rotate in response to their environment.

When water is more structured, the probe's color shifts. They quantify this with a number called GP: generalized polarization. Higher GP = more structured water. Lower GP = more fluid, bulk-like water.

Here's what they found:

**The metabolic oscillations only happen within a narrow window of water structure.**

Too structured? No oscillations. Too fluid? No oscillations.

*Oscillations only occur within a narrow range of water structure values.*

There's a sweet spot (a critical range) that is bounded on both sides by what mathematicians call supercritical Hopf bifurcations. Basically, within a narrow range, an oscillation exists. You could think of this like pacemaker cells in the heart - within specific ranges of electrolytes, they oscillate, but if you knock your electrolytes far enough off, they can stop.

They tested this across 25 different mutant yeast strains: wild type plus 24 mutants with knockouts in all sorts of proteins: glycolytic enzymes, mitochondrial components, vacuolar ATPases, cytoskeleton proteins. All mutations were unrelated to each other, but all shifted the water structure (the ACDAN GP value; the color of a water structure-sensitive dye).

The *only* parameter that predicted whether a strain would oscillate was water structure. It didn't matter what enzyme was knocked out, or how the biochemistry was altered by mutations. Just: how structured is your water?

Let that sink in for a second.

**The best predictor of whether a metabolic pathway oscillates is not the state of the enzymes in that pathway**. It's the physical state of the water surrounding them.

Correlation isn't causation, even though 25 unrelated perturbations pointed to water as the strongest predictor. So, to establish causality, they intervened in multiple other ways that directly impact the water:

**1. Heavy water (D2O).** Replace regular water with deuterium oxide. Same chemistry, heavier molecule. They found that the heavy water slows the oscillation frequency but doesn't change the amplitude. This is what you'd expect if water's rotational dynamics matter: heavier water rotates more slowly, so the cycle takes longer. But the system still oscillates because heavy water doesn't alter structuring, just how fast structure can change.

**2. Temperature shifts.** Raise the temperature and you push GP down (water becomes more fluid). They showed that heating cells from 25C to 35C during the oscillations kills them at the moment the water structure exits the critical range.

**3. Poison the ATP supply.** Add iodoacetate (blocks glycolysis) or 2-deoxyglucose (traps phosphate without producing ATP). Both killed oscillations once the GP moved out of the critical range. This is consistent with Ling's view that ATP acts as the trigger for protein-mediated water structuring, which the authors were well aware of.

**4. Break the cytoskeleton.** This is the most out-of-left-field result. Add Latrunculin B, which prevents actin from polymerizing. Oscillations vanish. Latrunculin doesn't affect glycolytic flux - the enzymes are still working at the same rate. The biochemistry is fine. What's broken is the physical scaffold that, according to the theory, structures the water.

*Metabolic oscillations removed after disrupting the cytoskeleton.*

Every single perturbation tells the same story: control the water state, control the oscillations. The chemistry follows the physics.

**A new kind of enzyme kinetics**

On the theoretical side, the group asked: if intracellular water is structured and behaves differently, should we still be modeling enzymes with the standard Michaelis-Menten kinetics -- equations that assume a dilute liquid?

So, they got rid of the yeast from the equation and just started working with the enzymes.

They tested two glycolytic enzymes (hexokinase and pyruvate kinase) in solutions crowded with PEG. Under Gilbert Ling's framework, this is a water-structuring polymer that behaves similarly to proteins in their "resting state," the highly structured state. If you concentrate it enough, classical Michaelis-Menten kinetics falls apart. What worked instead was the Yang-Ling adsorption isotherm, a statistical mechanical framework from Ling's hypothesis which was made decades ago in collaboration with Nobel Laureate CN Yang. Unlike Michaelis-Menten, this model naturally allows you to incorporate the state of the surrounding water as a variable.

Using this framework, they built a minimal model of glycolysis: ATP, ADP, and a variable *O* representing water order. The model reproduces the oscillations, the in-phase relationship between ATP and water structure, *and* the critical water structure window flanked by Hopf bifurcations.

*Predictions of metabolic oscillations from Yang-Ling isotherm plus water ordering.*

**So to recap:**

- **It is not natural to implement water order into mainstream models of the cell.**
- **Water structure was revealed as a global variable** that could control metabolic oscillations, **no matter what method you use to perturb it.**
- They made a model that uses Gilbert Ling's foundational equation, which predicts exactly how oscillations arise as a function of water order.

And here's what I find most exciting -- something the authors don't explicitly state but which follows directly from their model:

You can replace their water structure variable *O* with any other biophysical variable and predict coupling of any biophysical variable to biochemical processes in the cell!

With their model, we are allowed to consider any biophysical variable. Call such a variable O_x.

Any biophysical variable O_x that satisfies two conditions:

1. Driven by metabolism: dO_x/dt responds to ATP (or another metabolite)
2. Feeds back on metabolism: enzyme kinetics depend on O_x

...will show coupled oscillations with the biochemistry, and will have a critical window where oscillations are permitted.

For example, K+ satisfies both: ATP controls how much K+ is adsorbed to proteins, and free K+ concentration regulates glycolytic enzymes like PFK. So K+ should have its own critical window, just like water does.

Their model suggests they could have done the same thing with every variable in question! To alter the metabolic oscillations, they could have pushed K+, pH, and NADH out of range... and maybe even structure in the cell membrane?

**It doesn't stop at the cytoplasm**

Now for the cherry on top.

In a later paper, the group used a family of related probes with different affinities for water versus lipid environments: ACDAN (hydrophilic, lives in cytoplasm), PRODAN (intermediate), and LAURDAN (lipophilic, lives in membranes). They also used Nile red, which partitions into lipid droplets. Basically, they started to measure the membrane, not just the cytoplasm.

They found that all four probes oscillate at the same frequency during the metabolic oscillations.

But there was a slight time delay: the membrane-bound LAURDAN and Nile red oscillate in phase with each other, while the cytoplasmic ACDAN shows a slight phase difference. The signal propagates from the cytoplasm to the membranes, where glycolytic metabolism does not occur.

Their model predicted exactly this. If you couple a region of polarized, oscillating water to an adjacent region where no glycolysis occurs, e.g. a membrane, you get oscillations at the same frequency but with a phase shift. The water state in the cytoplasm is *transmitted* to water at membrane interfaces.

And since LAURDAN's fluorescence in membranes directly reports on lipid packing and order, this means the physical structure of the membrane is oscillating in sync with metabolism!

This connects directly to mainstream bioelectricity: it has been shown, including by Bagatolli's collaborator Thomas Heimburg, **that ion channel conductance depends directly on the thermodynamic state of the membrane**. Pure lipid membranes form voltage-gated channels near their phase transitions, and even protein channels like KcsA have their conductance and open-lifetime governed by the lipid membrane's physical state (Heimburg 2010; Blicher & Heimburg 2013).

So the conductance of the membrane, which in standard models is what sets the cell's voltage, is being driven by the physical state of the lipid, which is being driven by the water, which is being driven by metabolism.

The signal that controls bioelectricity is not biochemical. It's biophysical!

*For you mitochondriacs: they even showed Mitotracker red, a dye usually interpreted as a mitochondrial membrane potential indicator, oscillates at the same frequency.*

**So what?**

Let me bring this back to the three axioms:

**Generic Coupling**: In these yeast, ATP, NADH, K+, water structure, cell volume, heat flux, temperature, and membrane order all oscillate at the same frequency, and mutually influence each other.

**Biophysical Sufficiency**: You can turn oscillations on or off not by tweaking enzyme expression, but by pushing water structure in or out of a critical range with temperature, drugs, or cytoskeleton disruption.

**Tissue Coherence**: The oscillations only appear when cells are packed together at high density. Isolated cells don't oscillate. Something about physical proximity -- cells touching cells -- enables synchronization across billions of cells.

This is one organism, one metabolic process. But I think the principles are general. If biophysical variables are this tightly coupled in fermenting yeast, why would it be different in your neurons, your liver, your thymus, your tumors?

More on that soon.

-anabology

---

*Luis Bagatolli died in 2022 at 55. Gilbert Ling died in 2019 at 99. This is their work. I hope it gets the attention it deserves.*

**Papers:**

- Olsen, Stock & Bagatolli (2020). "Glycolytic oscillations and intracellular K+ concentration are strongly coupled in the yeast Saccharomyces cerevisiae." *Archives of Biochemistry and Biophysics.* DOI: 10.1016/j.abb.2020.108257
- Thoke, Thorsteinsson, Stock, Bagatolli & Olsen (2017). "The dynamics of intracellular water constrains glycolytic oscillations in Saccharomyces cerevisiae." *Scientific Reports.* DOI: 10.1038/s41598-017-16442-x
- Bagatolli, Stock & Olsen (2019). "Coupled Response of Membrane Hydration with Oscillating Metabolism in Live Cells: An Alternative Way to Modulate Structural Aspects of Biological Membranes?" *Biomolecules.* DOI: 10.3390/biom9110687
- Thoke, Bagatolli & Olsen (2018). "Effect of macromolecular crowding on the kinetics of glycolytic enzymes and the behaviour of glycolysis in yeast." *Integrative Biology.* DOI: 10.1039/c8ib00099a
- Heimburg (2010). "Lipid Ion Channels." *Biophysical Chemistry.* DOI: 10.1016/j.bpc.2010.02.018
- Blicher & Heimburg (2013). "Voltage-Gated Lipid Ion Channels." *PLoS ONE.* DOI: 10.1371/journal.pone.0065707
