// Re-render MathJax after each page load (when using Instant loading)
if (typeof MathJax !== 'undefined') {
    document$.subscribe(() => {
        MathJax.typesetPromise();
    });
}
