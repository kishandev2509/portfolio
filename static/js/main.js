
document.addEventListener("DOMContentLoaded", function () {
	const toggleBtn = document.getElementById("menu-toggle");
	const navLinks = document.getElementById("nav-links");
	let visible = false;

	toggleBtn.addEventListener("click", toggleMenuFn);
	heroImage.addEventListener("after");

	function toggleMenuFn() {
		if (!visible) {
			navLinks.classList.remove("hidden");
			Motion.animate(
				navLinks,
				{ height: ["0px", `${navLinks.scrollHeight}px`], opacity: [0, 1] },
				{ duration: 1, easing: "linear" }
			);
		} else {
			Motion.animate(
				navLinks,
				{ height: [`${navLinks.scrollHeight}px`, "0px"], opacity: [1, 0] },
				{ duration: 1, easing: "linear" }
			).finished.then(() => {
				navLinks.classList.add("hidden");
			});
		}
		visible = !visible;
	}
});
