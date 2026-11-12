// GitHub Actions supplies GITHUB_REPOSITORY for the repository being built.
export const repository = process.env.GITHUB_REPOSITORY || 'artemmanaenko/nadili_ro';
export const repositoryUrl = `https://github.com/${repository}`;
export const repositoryName = repository.split('/')[1];
