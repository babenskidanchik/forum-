
    async function loginUser() {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        const res = await fetch("http://127.0.0.1:8000/auth/login", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username, password})
        });

        const data = await res.json();
        alert(data.message || data.detail);

    }

    document.getElementById("loginButton").addEventListener("click", loginUser);

