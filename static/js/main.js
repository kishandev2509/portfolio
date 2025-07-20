document.documentElement.classList.toggle("dark", localStorage.theme === "dark");
// document.documentElement.classList.toggle(
// 	"dark",
// 	localStorage.theme === "dark" ||
// 		(!("theme" in localStorage) && window.matchMedia("(prefers-color-scheme: dark)").matches)
// );

function toggleTheme() {
	if (localStorage.theme === "dark") {
		localStorage.removeItem("theme");
		console.log("theme removed");
	} else {
		localStorage.theme = "dark";
		console.log("dark theme");
	}
	document.documentElement.classList.toggle("dark");
}

document.addEventListener("DOMContentLoaded", function () {
	const toggleBtn = document.getElementById("menu-toggle");
	const navLinks = document.getElementById("nav-links");
	toggleBtn.addEventListener("click", () => {
		toggleHeight(navLinks);
	});
	document.querySelectorAll(".motionHoverZoomIn").forEach((project_card) => hoverZoomIn(project_card));
});

let menuVisible = false;
function toggleHeight(elem) {
	if (!menuVisible) {
		elem.classList.remove("hidden");
		Motion.animate(
			elem,
			{ height: ["0px", `${elem.scrollHeight}px`], opacity: [0, 1] },
			{ duration: 1, easing: "linear" }
		);
	} else {
		Motion.animate(
			elem,
			{ height: [`${elem.scrollHeight}px`, "0px"], opacity: [1, 0] },
			{ duration: 1, easing: "linear" }
		).finished.then(() => {
			elem.classList.add("hidden");
		});
	}
	menuVisible = !menuVisible;
}

function hoverZoomIn(elem) {
	Motion.hover(elem, (el) => {
		Motion.animate(
			el,
			{ scale: 1.05, boxShadow: "0 10px 20px rgba(25, 49, 85, 0.2)" },
			{ duration: 0.2, easing: "ease-in-out" }
		);
		return () =>
			Motion.animate(
				el,
				{ scale: 1, boxShadow: "0 0 0 rgba(0, 0, 0, 0)" },
				{ duration: 0.1, easing: "ease-in-out" }
			);
	});
}
