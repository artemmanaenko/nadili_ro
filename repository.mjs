// GitHub Actions supplies GITHUB_REPOSITORY after a repository rename.
export const repository = process.env.GITHUB_REPOSITORY || 'artemmanaenko/ua_it_in_ro';
export const repositoryUrl = `https://github.com/${repository}`;
export const repositoryName = repository.split('/')[1];
