#bash script for converting pdfs to pngs
cd "../Desktop/comics"

find . -type f -name '*.pdf' -print0 |
  while IFS= read -r -d '' file
    do convert "${file}" "${file%.*}.png"
  done