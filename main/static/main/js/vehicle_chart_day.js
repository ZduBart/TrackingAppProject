async function getData(vehicleID, day, month, year) {
    let vehicleDetailsUrl = `/api/vehicles/${vehicleID}/details/?day=${day}&month=${month}&year=${year}`;

    const fetchData = await fetch(vehicleDetailsUrl);
    const jsonData = await fetchData.json();

    let coolantTemps = []
    let oilTemps = []
    let engineRPM = []
    let dts = []

    for (let i = 0; i < jsonData.length; i++) {
        let entry = jsonData[i];
        let coolantTemp = entry["coolant_temp"];
        let oilTemp = entry["oil_temp"];
        let engineRev = entry["engine_rpm"];
        let dt = entry["dt_log"];

        coolantTemps.push(coolantTemp);
        oilTemps.push(oilTemp);
        engineRPM.push(engineRev);
        dts.push(dt);
    }


    let outputGraphData = {
        labels: dts,
        datasets: [
            {
                label: 'Coolant temperature',
                data: coolantTemps,
                borderColor: "#ff0000",
                backgroundColor: "#79AEC8",
                fill: false,
            },
            {
                label: 'Oil temperature',
                data: oilTemps,
                borderColor: "#61f803",
                backgroundColor: "#79AEC8",
                fill: false,
            },
        ]
    };
    return outputGraphData;
}

function getConfig(data) {
    let config = {
        type: 'line',
        data: data,
        options: {
            animations: {
                tension: {
                    duration: 1000,
                    easing: 'easeInQuad',
                    from: 0.5,
                    to: 0,
                    loop: true
                }
            },

        }
    };
    return config;
}

async function getForm() {
    const form = document.getElementById('myForm');
    const data = Object.fromEntries(new FormData(form).entries());
    const urlArray = window.location.pathname.split('/');
    const vehicleID = urlArray[3];
    let parameterID = data['parameter_to_display'];
    let date = new Date(data['day_to_display']);
    let outputGraphData = await getData(vehicleID, date.getDate(), date.getMonth() + 1, date.getFullYear(), parameterID );

    let config = getConfig(outputGraphData);

    let ctx = document.getElementById('pie-chart').getContext('2d');

    if(window.myPie instanceof Chart){
        window.myPie.destroy();
    }
    window.myPie = new Chart(ctx, config);
}
