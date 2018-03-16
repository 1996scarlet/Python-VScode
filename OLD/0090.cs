    loggerFactory.AddConsole();
    env.EnvironmentName = EnvironmentName.Production;
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    else
    {
        app.UseExceptionHandler("/error");
    }

