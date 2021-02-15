export default function getCookies() {
    const cookies: { [name: string]: string; } = {};
    document.cookie
        .split(";")
        // Making sure they're not empty
        .filter(el => el.length)
        .map(c => c.split("=").map(i => i.trim()))
        .forEach(c => cookies[c[0]] = c[1]);
    return cookies;
}
