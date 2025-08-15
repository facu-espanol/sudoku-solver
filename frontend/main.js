document.getElementById('ping').onclick = async () => {
    const base = `http://${location.hostname}:8000`;
    const res = await fetch(`${base}/health`);
    document.getElementById('out').textContent = await res.text();
  };
  