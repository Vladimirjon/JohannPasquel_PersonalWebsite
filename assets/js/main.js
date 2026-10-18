(function () {
  var button = document.getElementById('copy-email');
  var toast = document.getElementById('toast');
  var email = document.querySelector('.email');
  if (!button || !toast || !email) return;

  var timer;
  function say(message) {
    toast.textContent = message;
    clearTimeout(timer);
    timer = setTimeout(function () { toast.textContent = ''; }, 3200);
  }

  button.addEventListener('click', function () {
    var text = email.textContent.trim();
    if (!navigator.clipboard) { say(button.dataset.failed); return; }
    navigator.clipboard.writeText(text).then(
      function () { say(button.dataset.copied); },
      function () { say(button.dataset.failed); }
    );
  });
})();
