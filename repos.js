fetch("https://api.github.com/orgs/hackmatelabs/repos?per_page=100&sort=updated")
  .then(r => r.json())
  .then(repos => {
    const el = document.getElementById("repos");
    const hide = [".github", "demo-repository", "whitepage"];
    for (const r of repos.filter(r => !hide.includes(r.name))) {
      const a = document.createElement("a");
      a.className = "repo";
      a.href = r.html_url;
      a.innerHTML = `<div class="name"></div><div class="desc"></div>`;
      a.querySelector(".name").textContent = r.name;
      a.querySelector(".desc").textContent = r.description || "";
      el.appendChild(a);
    }
  });
