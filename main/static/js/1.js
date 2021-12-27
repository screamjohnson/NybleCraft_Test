let change_themes=document.querySelector('#change_themes')
    change_themes.addEventListener('input',change_color)
let color=document.cookie
let regexp = /color=([^;\s]+)/;
let color_class = color.match(regexp)[1]
console.log(color_class)
document.body.style=`$background:${color_class};`
function change_color(e){

    document.body.style=`background:${e.target.value}`
    document.cookie=`color=${e.target.value}; path=/`
}
