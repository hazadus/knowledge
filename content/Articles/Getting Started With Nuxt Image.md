# Getting Started With Nuxt Image

![rw-book-cover](https://api.masteringnuxt.com/storage/ZUrrQkOQ7zWkVA0XR2grNxxh3fFS0YJLz6NWQJey.png)

## Metadata
- Author: [[masteringnuxt.com]]
- Full Title: Getting Started With Nuxt Image
- Category: #articles
- Document Note: Попробовать кэширование и кроп под разные размеры экрана на hazadus.ru.
- Document Tags: [[nuxt]] [[try]] 
- Summary: The NuxtImg component helps optimize images in your Nuxt app by allowing dynamic resizing, caching, and transformations with minimal code. It replaces standard img tags and automatically manages image quality and loading times based on user devices. With simple configuration, you can deliver fast-loading, high-quality images while improving your app's performance.
- URL: https://masteringnuxt.com/blog/getting-started-with-nuxt-image?friend=MOKKAPPS

## Highlights
- It *will* cache the images on your Nuxt server though.
  Instead of fetching directly from the `src` URL, your Nuxt server will fetch the image and cache it. If you inspect the devtools when using this component, you’ll see the actual `src` used by the underlying `img` tag is transformed to something like `/_ipx/w_800/<https://source.unsplash.com/blue-volkswagen-beetle-on-grass-field-7HNftpNvqho/6000x4000`>. ([View Highlight](https://read.readwise.io/read/01jcmv82ngxcj96ccx84a4d04z))


----
📂 [[Articles]] | Последнее изменение: 14.11.2024 20:54