function generatePassword() {
    const data = new URLSearchParams();
    data.append('length', document.getElementById('length').value);
    data.append('uppercase', document.getElementById('uppercase').checked);
    data.append('lowercase', document.getElementById('lowercase').checked);
    data.append('numbers', document.getElementById('numbers').checked);
    data.append('symbols', document.getElementById('symbols').checked);

    fetch('/generate', {
        method: 'POST',
        body: data
    })
    .then(res => res.json())
    .then(out => {
        if (out.error) return alert(out.error);
        document.getElementById('output').value = out.password;
        updateStrength(out.password);
    });
}

function copyPassword() {
    const pwd = document.getElementById('output');
    navigator.clipboard.writeText(pwd.value);
}

function updateStrength(password) {
    let score = 0;

    if (password.length >= 12) score += 25;
    if (/[A-Z]/.test(password)) score += 25;
    if (/[0-9]/.test(password)) score += 25;
    if (/[^A-Za-z0-9]/.test(password)) score += 25;

    const bar = document.getElementById('strength-bar');
    const text = document.getElementById('strength-text');

    bar.style.width = score + '%';

    if (score <= 25) {
        bar.className = 'progress-bar bg-danger';
        text.textContent = 'Weak';
    } else if (score <= 50) {
        bar.className = 'progress-bar bg-warning';
        text.textContent = 'Fair';
    } else if (score <= 75) {
        bar.className = 'progress-bar bg-info';
        text.textContent = 'Good';
    } else {
        bar.className = 'progress-bar bg-success';
        text.textContent = 'Strong';
    }
}