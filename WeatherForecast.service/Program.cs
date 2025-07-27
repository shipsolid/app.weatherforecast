// Create the web application builder with command line arguments
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer(); // Enable API explorer for endpoint discovery
builder.Services.AddSwaggerGen(); // Add Swagger documentation generation

// Build the web application from the configured builder
var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment()) // Only enable Swagger in development environment
{
    app.UseSwagger(); // Enable Swagger JSON endpoint
    app.UseSwaggerUI(); // Enable Swagger UI interface
}

app.UseHttpsRedirection(); // Redirect HTTP requests to HTTPS

// Array of weather condition descriptions for random selection
var summaries = new[]
{
    "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
};

// Map GET endpoint for weather forecast data
app.MapGet("/weatherforecast", () =>
{
    // Generate 5 days of weather forecast data with random temperature and conditions
    var forecast =  Enumerable.Range(1, 5).Select(index =>
        new WeatherForecast
        (
            DateOnly.FromDateTime(DateTime.Now.AddDays(index)), // Date for each day starting tomorrow
            Random.Shared.Next(-20, 55), // Random temperature in Celsius between -20 and 55
            summaries[Random.Shared.Next(summaries.Length)] // Random weather summary
        ))
        .ToArray();
    return forecast; // Return the generated forecast array
})
.WithName("GetWeatherForecast") // Set endpoint name for OpenAPI
.WithOpenApi(); // Enable OpenAPI documentation for this endpoint

// Start the web application and begin listening for requests
app.Run();

// Record type representing a weather forecast entry
record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    // Computed property to convert Celsius to Fahrenheit
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
