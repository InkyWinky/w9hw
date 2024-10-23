var vg_1 = "https://raw.githubusercontent.com/InkyWinky/w9hw/refs/heads/main/plan_crash_symbol_map.vg.json";
vegaEmbed("#plane_crash_map", vg_1).then(function(result) {
}).catch(console.error);
var vg_2 = "https://raw.githubusercontent.com/InkyWinky/w9hw/refs/heads/main/transport_safety.vg.json";
vegaEmbed("#transport_safety_bar", vg_2).then(function(result) {
}).catch(console.error);
var vg_3 = "https://raw.githubusercontent.com/InkyWinky/w9hw/refs/heads/main/aus_plane_crash_map.vg.json";
vegaEmbed("#aus_crash_map", vg_3).then(function(result) {
}).catch(console.error);
var vg_4 = "https://raw.githubusercontent.com/InkyWinky/w9hw/refs/heads/main/crash_years_line.vg.json";
vegaEmbed("#crashes_per_year_line", vg_4,{"actions": false}).then(function(result) {
}).catch(console.error);
var vg_5 = "https://raw.githubusercontent.com/InkyWinky/w9hw/refs/heads/main/time_crashes_radial.vg.json";
vegaEmbed("#time_crashes_radial", vg_5,{"actions": false}).then(function(result) {
}).catch(console.error);

