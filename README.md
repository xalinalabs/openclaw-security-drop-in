
async function fetchLogs(){
 const res = await fetch('/api/logs');
 const logs = await res.json();
 document.getElementById('logs').innerText = JSON.stringify(logs,null,2);
}
setInterval(fetchLogs,2000);
fetchLogs();
