paper.install(window);

createTreeCrown = function(startPoint, blueprint, age) {


}

window.onload = function() {
	paper.setup("Tree");

	var lines = [];
	var blueprint = [];

	var tool = new Tool();
	var stem = new Path.Line(view.center.subtract(new Point(0, -200)), view.center);
	stem.strokeColor = "#d8dee9";
	var line = new Path.Line(view.center, view.center);
	line.strokeColor = "#d8dee9";

	tool.onMouseMove = function(event) {
		line.segments[1].point = event.point;
	}

	tool.onMouseDown = function(event) {
		var newLine = new Path.Line(view.center, event.point)
		newLine.strokeColor = "#d8dee9";

		lines.push(newLine);
		blueprint.push(event.point);
	}

	view.draw();
}