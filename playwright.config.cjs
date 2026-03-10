module.exports = {
  testDir: './tests',
  timeout: 60000,
  use: {
    headless: false,
    viewport: { width: 390, height: 844 },
    launchOptions: {
      slowMo: 1500,
    },
  },
  projects: [
    {
      name: 'chromium',
      use: { browserName: 'chromium' },
    },
  ],
};
