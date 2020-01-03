addToHomescreen({
  appID: "com.herokuapp.hvlia",
             appName: "HVLIA",
             lifespan: 150,
             autostart: true,
             skipFirstVisit: false,
             minSessions: 1,
             displayPace: 0,
             customPrompt: {
                 title: "Install HVLIA?",
                 src: "static/images/icons/icon-96x96.png",
                 cancelMsg: "Cancel",
                 installMsg: "Install"
             }

});
