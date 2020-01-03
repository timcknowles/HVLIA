addToHomescreen({
  appID: "com.herokuapp.hvlia",
             appName: "HVLIA",
             lifespan: 15,
             autostart: true,
             skipFirstVisit: true,
             minSessions: 1,
             displayPace: 0,
             customPrompt: {
                 title: "Install HVLIA?",
                 src: "static/images/icons/icon-96x96.png",
                 cancelMsg: "Cancel",
                 installMsg: "Install"
             }

});
