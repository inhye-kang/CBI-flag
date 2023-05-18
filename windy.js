const options = {
    key: 'ITliu3zYrbdKunwcCKDJWIhCPDaYEktg', // REPLACE WITH YOUR KEY !!!

    verbose: true,

    // Optional: Initial state of the map
    lat: 50.4,
    lon: 14.3,
    zoom: 5
    // Tip: Use verbose true for nice console output
    // verbose: true
};

windyInit(options, windyAPI => {
    const { store, broadcast } = windyAPI;
    const windSpeed = data.daypart[0].windSpeed[0];
    const windGust = data.daypart[0].windGust[0];
    const temperature = data.daypart[0].temperature[0];

    // Round the data to two decimal places
    const windSpeedRounded = parseFloat(windSpeed.toFixed(2));
    const windGustRounded = parseFloat(windGust.toFixed(2));
    const temperatureRounded = parseFloat(temperature.toFixed(2));

    // Print the rounded data
    console.log(`Wind Speed: ${windSpeedRounded}`);
    console.log(`Wind Gust: ${windGustRounded}`);
    console.log(`Temperature: ${temperatureRounded}`);
    let i = 0;

    setInterval(() => {
        i = i === 3 ? 0 : i + 1;
        store.set('overlay', overlays[i]);
    }, 800);

    // Observe the most important broadcasts
    broadcast.on('paramsChanged', params => {
        console.log('Params changed:', params);
    });

    broadcast.on('redrawFinished', params => {
        console.log('Map was rendered:', params);
    });
});