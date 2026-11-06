import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";
const path = "D:/Desktop/ai建议表格.xlsx";
const input = await FileBlob.load(path);
const wb = await SpreadsheetFile.importXlsx(input);
const s = await wb.inspect({kind:"workbook,sheet,table", maxChars:30000, tableMaxRows:15, tableMaxCols:15, tableMaxCellChars:100});
console.log(s.ndjson);
