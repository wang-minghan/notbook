import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
const wb = await SpreadsheetFile.importXlsx(await FileBlob.load("D:/Desktop/ai建议表格.xlsx"));
for (const sh of wb.worksheets.items) {
  const f = await wb.inspect({kind:"formula", sheetId:sh.name, maxChars:3000, options:{maxResults:100}});
  const d = await wb.inspect({kind:"drawing", sheetId:sh.name, maxChars:1000});
  console.log(`SHEET ${sh.name}\nFORMULAS\n${f.ndjson}\nDRAWINGS\n${d.ndjson}`);
}
