import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.varun.prio',
  appName: 'Prio',

  webDir: 'dist',

  server: {
    androidScheme: 'https',
    // Agar Gemini/AI call karna hai live, hostname set karo
    // hostname: 'app.sahutracker.com',
    allowNavigation: [
      'generativelanguage.googleapis.com',
      '*.workers.dev',
      'fonts.googleapis.com',
      'fonts.gstatic.com',
      'cdnjs.cloudflare.com',
      'cdn.jsdelivr.net',
      'api.dicebear.com'
    ],
  },

  android: {
    backgroundColor: '#3b0764',
    allowMixedContent: false,
    captureInput: true,
    webContentsDebuggingEnabled: false,
    overrideUserAgent: 'Prio-Android/1.0',
  },

  ios: {
    backgroundColor: '#3b0764',
    contentInset: 'automatic',
    scrollEnabled: false,
    overrideUserAgent: 'Prio-iOS/1.0',
  },

  plugins: {
    SplashScreen: {
      launchShowDuration: 1500,
      launchAutoHide: true,
      backgroundColor: '#000000',
      androidSplashResourceName: 'splash',
      androidScaleType: 'CENTER_INSIDE',
      showSpinner: false,
      splashFullScreen: true,
      splashImmersive: true,
    },

    StatusBar: {
      style: 'DARK',
      backgroundColor: '#3b0764',
      overlaysWebView: false,
    },

    LocalNotifications: {
      smallIcon: 'ic_stat_icon_config_sample',
      iconColor: '#7c5cff',
      sound: 'message_sound.mp3',
    },

    GoogleAuth: {
      scopes: ['profile', 'email'],
      serverClientId: '1092220613288-0624a0kmdedokdf1158e239ckq1ts1n0.apps.googleusercontent.com',
      forceCodeForRefreshToken: true,
    },
  },
};

export default config;
