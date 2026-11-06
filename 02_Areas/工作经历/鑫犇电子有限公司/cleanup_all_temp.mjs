import fs from 'node:fs/promises';
const cwd='C:/Users/mingh/OneDrive/notebook/02_Areas/工作经历/鑫犇电子有限公司';
const names=['inspect_ai_template.mjs','inspect_ai_details.mjs','inspect_governance.mjs','inspect_active_templates.mjs','pre_edit_inspect.mjs','apply_template_optimization.mjs','patch_balance.mjs','verify_outputs.mjs','final_scan.mjs','active_scan.mjs','scan_active_xlsx_terms.mjs','update_encoding_governance.mjs','finish_encoding_alignment.mjs','finish_ops_gov_erd.mjs','retry_prod_alignment.mjs','cleanup_tmp.mjs','check_prod_headers.mjs','verify_encoding_alignment.mjs'];
for(const n of names){try{await fs.unlink(cwd+'/'+n)}catch{}}
const out=cwd+'/outputs/20261106_template_优化'; for(const n of await fs.readdir(out)){if(n.endsWith('.inspect.ndjson')){try{await fs.unlink(out+'/'+n)}catch{}}}
console.log('temporary scripts and inspection dumps removed');
