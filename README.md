[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/serhii73/find_the_site/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/serhii73/find_the_site.svg)](https://GitHub.com/serhii73/find_the_site/graphs/contributors/)
[![GitHub stars](https://img.shields.io/github/stars/serhii73/find_the_site.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/serhii73/find_the_site/stargazers/)
![GitHub forks](https://img.shields.io/github/forks/serhii73/find_the_site.svg?style=social)
[![GitHub issues](https://img.shields.io/github/issues/serhii73/find_the_site.svg)](https://GitHub.com/serhii73/find_the_site/issues/)

# find_the_site
## Are you looking for a company/enterprise website? This small library finds websites in [duckduckgo search engine](https://duckduckgo.com/?t=hk)
#### Optionally you can use:
- the [ecosia](https://ecosia.org) search engine, to support environmental efforts
##### How to Install ?

```
pip install find_the_site
```

##### How to use ?
```
In [1]: from find_the_site.fw import get_website 
In [2]: get_website("UNITED NATIONS", eco=True)                                
Out[2]: 
['http://www.un.org/en/',
 'https://en.wikipedia.org/wiki/United_Nations',
 'https://www.undp.org/content/undp/en/home.html',
 'https://scholarshipscorner.website/united-nations/',
 'https://www.unenvironment.org/',
 'https://unnwo.org/',
 'https://peacekeeping.un.org/en',
 'https://www.unodc.org/',
 'https://careers.un.org/',
 'https://www.unicef.org/']

```
