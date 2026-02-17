    async function registerUser() {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        const repeat = document.getElementById("repeat").value

        if (password != repeat) {
            alert("Passwords do not match!")
            return;
        }

        const res = await fetch("http://127.0.0.1:8000/auth/register", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username, password})
        });

        const data = await res.json();

        if (res.ok) {
            alert(data.message);
            window.location.href = '/';
        } else {
            alert(data.detail || 'Error')
        }
    }

    document.getElementById("registerBtn").addEventListener("click", registerUser);
