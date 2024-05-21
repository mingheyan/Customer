function getTodayTime() {
  // Get current time
  var day = new Date();
  let seconds = day.getSeconds();
  if (seconds < 10) {
    seconds = "0" + seconds;
  } else {
    seconds = seconds;
  }
  let minutes = day.getMinutes();
  if (minutes < 10) {
    minutes = "0" + minutes;
  } else {
    minutes = minutes;
  }
  let time = day.getFullYear() + "-" + (day.getMonth() + 1) + "-" + day.getDate() + " " + day.getHours() + ":" + minutes + ":" + seconds;
  return time;
}

