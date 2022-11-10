# Global Metrics Visualizer

## 1. Introduction

This project is a free tool for anyone to visualize and understand global metrics related to CO2 emissions.
You can also fork the project and experiment with your own metrics! Just plug in data in the same format and see what insights you can find!

## 2. Navigation

Simply visit <link to dashboard> to explore the output. Or clone the repo and run the `dashboard.bat` file to run it locally!

For those who want to dive even deeper, you can explore the visualization notebooks and the modify  parameters. Just customize the variables in **Visualization Parameters** such as countries to visualize, metrics to visualize, etc.

Finally, you can customize the data prep or forecast scripts and expand them to build a bigger system.
  
## 3. File Structure

### Main Pipeline Scripts

- `1_data_prep_notebooks`: The data preparation scripts ordered as `D1_join_metric_data`, `D2_data_enrichment`. Output of `D2` is used for `M1` and visualizations.
- `2_enrichment_models_notebooks`: Currently only has `M1_forecast_metric` to forecast CO2 emissions per country.
- `3_viz_notebooks`: Visualization Notebooks for the above output.

### Data

- The raw datasets and datasets generated in pipelines.

### Dahsboard

- The interactive dashboard webapp implamented in Plotly

## Ciatations

**ourworldindata.org template**  
`Hannah Ritchie, Max Roser and Pablo Rosado (2020) - "CO₂ and Greenhouse Gas Emissions". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions' [Online Resource]`
