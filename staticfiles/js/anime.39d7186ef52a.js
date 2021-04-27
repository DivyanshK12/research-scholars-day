gsap.registerPlugin(ScrollToPlugin);
gsap.registerPlugin(ScrollTrigger);
ScrollTrigger.defaults({
    toggleActions: "play reset play reset",
  });

gsap.from("#profile", {opacity: 0, scrollTrigger: "#profile", y: 100, duration: 1});
function por()
{
    gsap.to(window, {duration: 1, scrollTo: "#por", ease: "power2"});
    return false;
}

function mission()
{
    gsap.to(window, {duration: 1, scrollTo: "#mission", ease: "power2"});
    return false;
}
function go_bottom()
{
    gsap.to(window, {duration: 1, scrollTo: {y: "max"}, ease: "power2"});
    return false;
}
function go_top()
{
    gsap.to(window, {duration: 1, scrollTo: {y: "min"}, ease: "power2"});
    return false;
}