function getUserInfo() {
  const urlParams = new URLSearchParams(window.location.search);
  const token = urlParams.get("token");
  if (token) {
    const decoded = jwt_decode(token);
    document.getElementById(
      "user_info"
    ).innerText = `User ID: ${decoded.user_id}\nUsername: ${decoded.username}\nFirst Name: ${decoded.first_name}\nLast Name: ${decoded.last_name}`;
  }
}
window.onload = getUserInfo;
