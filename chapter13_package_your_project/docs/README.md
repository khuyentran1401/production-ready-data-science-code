# Documentation Directory

This directory will contain the generated HTML documentation when you run:

```bash
pdoc --html pandas_processors -o docs
```

As shown in Chapter 13, this command generates API documentation from your code's docstrings.

## Generated Structure

After running the pdoc command, this directory will contain:

```
docs/
└── pandas_processors/
    ├── create.html
    ├── impute.html 
    ├── index.html
    └── normalize.html
```

## Hosting Documentation

The generated documentation can be hosted on GitHub Pages by:

1. Committing the docs directory to your repository
2. Configuring GitHub Pages to serve from the docs folder
3. Your documentation will be available at: `https://username.github.io/pandas-processors/`

For detailed setup instructions, see the [GitHub Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).