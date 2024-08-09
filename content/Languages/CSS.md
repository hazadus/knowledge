# Основы CSS

> [!info] Основы CSS - Изучение веб-разработки | MDN  
> CSS (Cascading Style Sheets) - это код, который вы используете для стилизации вашей веб-страницы.  
> [https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/CSS_basics](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/CSS_basics)  
## Docs

> [!info] Guides Archive - CSS-Tricks  
> This guide is about the HTML syntax for responsive images (and a little bit of CSS for good measure).  
> [https://css-tricks.com/guides/](https://css-tricks.com/guides/)  

> [!info] A Complete Guide to Flexbox | CSS-Tricks  
> Our comprehensive guide to CSS flexbox layout.  
> [https://css-tricks.com/snippets/css/a-guide-to-flexbox/#flexbox-background](https://css-tricks.com/snippets/css/a-guide-to-flexbox/#flexbox-background)  
## Design

> [!info] Color Palettes  
> W3Schools offers free online tutorials, references and exercises in all the major languages of the web.  
> [https://www.w3schools.com/colors/colors_palettes.asp](https://www.w3schools.com/colors/colors_palettes.asp)  

> [!info] Google Fonts  
> Making the web more beautiful, fast, and open through great typography  
> [https://fonts.google.com/](https://fonts.google.com/)  

> [!info] Force bootstrap responsive image to be square  
> Thanks for contributing an answer to Stack Overflow!  
> [https://stackoverflow.com/questions/23400232/force-bootstrap-responsive-image-to-be-square](https://stackoverflow.com/questions/23400232/force-bootstrap-responsive-image-to-be-square)  
### margin
[https://doka.guide/css/margin/](https://doka.guide/css/margin/)
```CSS
div {
	margin: 10px 20px 30px 40px; /* clockwise top-right-bottom-left */
	margin: 10px 20px; /* top=bottom=10px, left=right=20px */
	margin: 10px; /* all=10px */
	margin: 10px 20px 30px; /* top=10 left=right=20 bottom=30 */
	paddin: 10px; /* used just like margin! */
}
```
Марджины у блочных элементов расположенных друг под другом не суммируются, а выбирается один – наибольший из двух.
### opacity / alpha-channel in rgba()
Opacity регулирует прозрачность всего блока, включая то, что в нем находится. Последний параметр в `rgba()` регулирует прозрачность цвета. Например, если в блоке поставить `background: rgba(0, 0, 0, 0.5);` – блок (фон) будет полупрозрачный, а текст в нём абсолютно непрозрачный.
### background
![[attachments/Untitled 21.png|Untitled 21.png]]
`background-size: cover;` заставит фон закрыть всю площадь блока, а `background-size: contain;` сделает так, чтобы картинка была видна целиком.
### list-style
Для `ul`, `ol` можно задать `list-style: none;` чтобы слева не было маркеров.
### cursor
`cursor: pointer;` делает так, чтобы курсор над элементом оставался обычной стрелкой.
# Recipes

> [!info] A collection of popular layouts and patterns made with CSS - CSS Layout  
> A collection of popular layouts and patterns made with CSS  
> [https://csslayout.io/](https://csslayout.io/)  

> [!info] Tree views in CSS  
> How to create a tree view (collapsible list) using only HTML and CSS  
> [https://iamkate.com/code/tree-views/](https://iamkate.com/code/tree-views/)  

> [!info] Rebuilding a comment component with modern CSS  
> Building a comment component with modern CSS like flexbox, logical properites, :has, style queries, and subgrid.  
> [https://ishadeed.com/article/comment-component/](https://ishadeed.com/article/comment-component/)  

> [!info] CSS Infinite Slider Flipping Through Polaroid Images | CSS-Tricks  
> In the last article, we made a pretty cool little slider (or "carousel" if that's what you prefer) that rotates in a circular direction.  
> [https://css-tricks.com/css-infinite-slider-flipping-through-polaroid-images/?mkt_tok=MTEzLURUTi0yNjYAAAGIzwijD1AnIGJ73j6HQPOxHkGpi9-Kiwctm-bjqHivTTRwpvkrk6SKnsUHWV2KT2eiu8PX9_Fq7Me_vYP0Fqgrxv1TQ1jcq3Ta81oOaPZEEpfE](https://css-tricks.com/css-infinite-slider-flipping-through-polaroid-images/?mkt_tok=MTEzLURUTi0yNjYAAAGIzwijD1AnIGJ73j6HQPOxHkGpi9-Kiwctm-bjqHivTTRwpvkrk6SKnsUHWV2KT2eiu8PX9_Fq7Me_vYP0Fqgrxv1TQ1jcq3Ta81oOaPZEEpfE)  

> [!info] CSS Infinite and Circular Rotating Image Slider | CSS-Tricks  
> Image sliders (also called carousels) are everywhere.  
> [https://css-tricks.com/css-only-infinite-and-circular-image-slider/](https://css-tricks.com/css-only-infinite-and-circular-image-slider/)  

> [!info] CSS Infinite 3D Sliders | CSS-Tricks  
> In this series, we've been making image sliders with nothing but HTML and CSS.  
> [https://css-tricks.com/css-infinite-3d-sliders/](https://css-tricks.com/css-infinite-3d-sliders/)  
# References

> [!info] CSS Selectors: A Visual Guide & Reference  
> Visual guide to CSS selectors, including pseudo-classes (:nth-child, :hover,.  
> [https://fffuel.co/css-selectors/](https://fffuel.co/css-selectors/)