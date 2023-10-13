console.log('cos tam');

Pusher.logToConsole = true;

let pusher = new Pusher('47525134414d50e400a5', {
  cluster: 'eu'
});

let channel = pusher.subscribe('my-channel');



channel.bind('my-event', function (data) {
  console.log(JSON.stringify(data));
  // update chart
});
