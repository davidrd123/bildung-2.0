# Normalized Extracts

Corrected working extracts live here.

Normalization may repair the systematic long-s OCR artifact (`f → s` in non-final positions, validated against a Latin lexicon), reassemble line-end hyphenation, and remove or relocate marginalia and headers that the raw extractor preserved inline. It should not silently emend the text.

If a reading depends on a corrected character that ABBYY flagged `suspicious="1"` or `wordFromDictionary="0"`, note it in the extract or in `../page-map.yaml`.
