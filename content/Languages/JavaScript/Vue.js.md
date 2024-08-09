Basic Vue stuff
Create Vue project
Templates
Class and Style Bindings
List Rendering
v-for for Component
Tools
VSCode Extensions
Tutorials
API
Component Libraries
Components

> [!info] Combining Flask and Vue  
> So you've finally got Flask under your belt, and you're no stranger to JavaScript.  
> [https://testdriven.io/blog/combine-flask-vue/#jinja-template](https://testdriven.io/blog/combine-flask-vue/#jinja-template)  

> [!info] Developing a Single Page App with Flask and Vue.js  
> The following is a step-by-step walkthrough of how to set up a basic CRUD app with Vue and Flask.  
> [https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/](https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/)  
## Basic Vue stuff
### Create Vue project
```Bash
vue create vueapp
```
### Templates
Inserting raw HTML from variable into template [https://vuejs.org/guide/essentials/template-syntax.html#raw-html](https://vuejs.org/guide/essentials/template-syntax.html#raw-html)
```HTML
<p>Using text interpolation: {{ rawHtml }}</p>
<p>Using v-html directive: <span v-html="rawHtml"></span></p>
```
Dynamically binding multiple attributes [https://vuejs.org/guide/essentials/template-syntax.html#dynamically-binding-multiple-attributes](https://vuejs.org/guide/essentials/template-syntax.html#dynamically-binding-multiple-attributes)
```HTML
data() {
  return {
    objectOfAttrs: {
      id: 'container',
      class: 'wrapper'
    }
  }
}
<div v-bind="objectOfAttrs"></div>
```
### Class and Style Bindings
Link: [https://vuejs.org/guide/essentials/class-and-style.html#binding-html-classes](https://vuejs.org/guide/essentials/class-and-style.html#binding-html-classes)
```HTML
<div :class="{ active: isActive }"></div>
```
The above syntax means the presence of the `active` class will be determined by the [**truthiness**](https://developer.mozilla.org/en-US/docs/Glossary/Truthy) of the data property `isActive`.
![[attachments/Untitled 34.png|Untitled 34.png]]
### List Rendering
Link: [List Rendering | Vue.js (vuejs.org)](https://vuejs.org/guide/essentials/list.html)
![[attachments/Untitled 1 13.png|Untitled 1 13.png]]
### v-for for Component
Link: [https://vuejs.org/guide/essentials/list.html#v-for-with-a-component](https://vuejs.org/guide/essentials/list.html#v-for-with-a-component)
![[attachments/Untitled 2 11.png|Untitled 2 11.png]]
## Tools
### VSCode Extensions

> [!info] The Best VS Code Extensions For Vue Developers  
> Adding the right VS Code Extensions to Visual Studio can make your life as a developer so much easier.  
> [https://learnvue.co/tutorials/best-vscode-extensions](https://learnvue.co/tutorials/best-vscode-extensions)  
## Tutorials
### API

> [!info] Get Kanye West Quotes w/ Vue and Axios - Beginner's Guide to APIs  
> Axios is one of the most popular HTTP request libraries for JavaScript, and it's commonly used to call APIs inside of Vue apps.  
> [https://learnvue.co/tutorials/vue-and-axios](https://learnvue.co/tutorials/vue-and-axios)  
## Component Libraries

> [!info] The Top 20 Vue Component Libraries in 2022  
> As fun as it can be to build everything yourself in Vue, there are so many awesome libraries out there.  
> [https://learnvue.co/tutorials/top-vue-component-libraries](https://learnvue.co/tutorials/top-vue-component-libraries)  
### Components

> [!info] Introduction | vue3-easy-data-table  
> vue3-easy-data-table is a customizable and easy-to-use data table component made with Vue.  
> [https://hc200ok.github.io/vue3-easy-data-table-doc/introduction.html](https://hc200ok.github.io/vue3-easy-data-table-doc/introduction.html)  
https://github.com/SortableJS/vue.draggable.next