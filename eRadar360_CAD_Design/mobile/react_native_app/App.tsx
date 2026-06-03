import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import { StyleSheet } from 'react-native';
import { Colors } from './src/theme';
import { HomeScreen } from './src/screens/HomeScreen';
import { SearchScreen } from './src/screens/SearchScreen';
import { ProfileScreen } from './src/screens/ProfileScreen';

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <GestureHandlerRootView style={appStyles.root}>
      <SafeAreaProvider>
        <NavigationContainer>
          <Tab.Navigator screenOptions={{
            headerShown: false,
            tabBarStyle: { backgroundColor: '#1A1A1A', borderTopColor: '#333', paddingBottom: 4, height: 60 },
            tabBarActiveTintColor: Colors.primary,
            tabBarInactiveTintColor: '#666',
          }}>
            <Tab.Screen name='Radar' component={HomeScreen} />
            <Tab.Screen name='Alerts' component={SearchScreen} />
            <Tab.Screen name='Map' component={ProfileScreen} />
            <Tab.Screen name='Settings' component={ProfileScreen} />
          </Tab.Navigator>
        </NavigationContainer>
      </SafeAreaProvider>
    </GestureHandlerRootView>
  );
}

const appStyles = StyleSheet.create({ root: { flex: 1 } });
