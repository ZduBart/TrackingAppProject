async function getData(day, month, year) {
    let vehicleDetailsUrl = `/api/vehicles/1/details/?day=${day}&month=${month}&year=${year}`;

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
    }

    window.onload = () => {
        let outputGraphData = getData(18, 5, 2022).then((outputGraphData) => {
        let config = getConfig(outputGraphData);
        console.log(outputGraphData);
        console.log(config);
        let ctx = document.getElementById('pie-chart').getContext('2d');
        window.myPie = new Chart(ctx, config);
    });
    };
