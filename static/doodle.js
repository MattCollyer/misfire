var doodle = d3.select('#doodle');
var data = JSON.parse(doodle.attr('data'));
doodle.attr('data', null);
if (doodle.attr('class') == 'reveal') {
	var stroke = 5;
} else {
	var stroke = 3;
}
var svg = doodle.append('svg').attr('viewBox', '0 0 256 256');
data.forEach(function(e) {
	var points = [];
	for (var i = 0; i < e[0].length; i++) {
		var point = {
			"x": e[0][i],
			"y": e[1][i]
		}
		points.push(point);
	}
	var line =  d3.line()
				  .x(function(d) { return d.x; })
				  .y(function(d) { return d.y; })
				  .curve(d3.curveBasis);
	svg.append('path')
	   .attr('fill', 'none')
	   .attr('stroke', 'black')
	   .attr('stroke-width', stroke)
		 .attr('stroke-linecap', 'round')
	   .attr('d', line(points));
});
