library(tidyverse)
read_csv("model_output/modelC_sim.csv")  %>% 
  group_by(simID) %>% 
  mutate(state = paste0(IL6, IL6_hi, IP10, IP10_hi, MCP1, MCP1_hi, MIG)) %>%
  mutate(state.0 = first(state)) %>% 
  mutate(`IL-6` = IL6 + IL6_hi,
         `IP-10` = IP10 + IP10_hi,
         `MCP-1` = MCP1 + MCP1_hi,
         MIG = MIG) %>%
  gather(cytokine, sim.value, `IL-6`, `IP-10`, `MCP-1`, MIG) %>%
  #re-order the cytokines for the plot
  mutate(cytokine = factor(cytokine, levels = c("IL-6", "MCP-1", "MIG", "IP-10"))) %>% 
  ungroup %>%
  #The simulations may cover the same initial condition more than once so remove duplicates 
  distinct(state.0, state, timepoint,cytokine, .keep_all = T) %>%
  #Only plot until 10 timesteps
  filter(timepoint < 11 ) %>% 
  ggplot(data = .,aes(x = timepoint, y = sim.value)) +
  theme_bw() +
  stat_summary(geom="line", fun.y=mean)+
  stat_summary(geom="point", fun.y=mean)+ 
  stat_summary(fun.data = mean_sdl, geom = "errorbar", width = 0.5, fun.args = list(mult = 1)) +
  facet_grid(  cytokine ~ injury) + theme(legend.position = "right") -> p

