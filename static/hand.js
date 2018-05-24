function wrapCharacters(e, t) {
		$(e).contents().each(function() {
				if (1 === this.nodeType)
						wrapCharacters(this);
				else if (3 === this.nodeType) {
						var e = this.nodeValue.trim();
						$(this).replaceWith($.map(e.split(""), t).join(""))
				}
		})
}
function ShuffleHandwrittenText(e) {
		wrapCharacters(e, function(e) {
				var t = Math.ceil(3 * Math.random());
				return "9" == e && (t = 2), '<span class="font-' + t + '">' + e + "</span>"
		})
}
ShuffleHandwrittenText($(".hand"));
var guess = $("#guess");
if (guess[0] != null) {
	guess.addClass("font-"+Math.ceil(3 * Math.random()));
}
