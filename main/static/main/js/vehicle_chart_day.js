async function getData(vehicleID, day, month, year) {
    let vehicleDetailsUrl = `/api/vehicles/${vehicleID}/details/?day=${day}&month=${month}&year=${year}`;

    const fetchData = await fetch(vehicleDetailsUrl);
    const jsonData = await fetchData.json();


    let coolantTemps = []
    let dts = []

    for (let i = 0; i < jsonData.length; i++) {
        let entry = jsonData[i];
        let temp = entry["coolant_temp"];
        let dt = entry["dt_log"];

        dts.push(dt);
        coolantTemps.push(temp);
    }

    console.log(coolantTemps);
    console.log(dts);

    let outputGraphData = {
        labels: dts,
        datasets: [
            {
                label: 'Coolant temperature',
                data: coolantTemps,
                borderColor: "#ff0000",
                backgroundColor: "#79AEC8",
                fill: false,
                tension: 0
            },
        ]
    };
    console.log(outputGraphData);
    return outputGraphData;
}


function getConfig(data) {
    let config = {
        type: 'line',
        data: data,
        options: {
            scales: {
                y: {
                    // beginAtZero: true,

                }
            }
        },
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Chart.js Line Chart'
            }
        },
    };
    return config;
};

// window.onload = () => {
//     var pathArray = window.location.pathname.split('/');
//     var secondLevelLocation = pathArray[3];
//     console.log(secondLevelLocation);
// };

function getForm() {
    const form = document.getElementById('myForm');
    const data = Object.fromEntries(new FormData(form).entries());
    const urlArray = window.location.pathname.split('/');
    const vehicleID = urlArray[3];
    console.log(vehicleID);
    let date = new Date(data['day_to_display']);
    let outputGraphData = getData(vehicleID, date.getDate(), date.getMonth() + 1, date.getFullYear()).then((outputGraphData) => {
        let config = getConfig(outputGraphData);
        console.log(outputGraphData);
        console.log(config);

        let ctx = document.getElementById('pie-chart').getContext('2d');
        window.myPie = new Chart(ctx, config);

        console.log(date.getDate());
        console.log(date.getMonth());
        console.log(date.getFullYear());

    })
}
