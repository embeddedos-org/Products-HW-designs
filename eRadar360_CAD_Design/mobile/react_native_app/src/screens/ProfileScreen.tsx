import React, { useState } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Switch } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Colors, Typography, Spacing, BorderRadius } from '../theme';

export const ProfileScreen: React.FC = () => {
  const [notificationsEnabled, setNotificationsEnabled] = useState(true);
  const [darkMode, setDarkMode] = useState(true);
  return (
    <SafeAreaView style={profileStyles.safe} testID='profile-screen'>
      <ScrollView contentContainerStyle={profileStyles.content}>
        <View style={profileStyles.avatar} testID='avatar'>
          <Text style={profileStyles.avatarText}>U</Text>
        </View>
        <Text style={profileStyles.name} testID='user-name'>User</Text>
        <Text style={profileStyles.app} testID='app-label'>eRadar360_CAD</Text>
        <View style={profileStyles.statsRow}>
          {[['0','Saved'],['0','Activity'],['v1.0','Version']].map(([v,l]) => (
            <View key={l} style={profileStyles.stat} testID={'stat-' + l.toLowerCase()}>
              <Text style={profileStyles.statValue}>{v}</Text>
              <Text style={profileStyles.statLabel}>{l}</Text>
            </View>
          ))}
        </View>
        <View style={profileStyles.section}>
          <Text style={profileStyles.sectionTitle}>Preferences</Text>
          <View style={profileStyles.row} testID='notifications-row'>
            <Text style={profileStyles.rowLabel}>Notifications</Text>
            <Switch value={notificationsEnabled} onValueChange={setNotificationsEnabled} trackColor={{ true: Colors.primary }} testID='notifications-switch' />
          </View>
          <View style={profileStyles.row} testID='darkmode-row'>
            <Text style={profileStyles.rowLabel}>Dark Mode</Text>
            <Switch value={darkMode} onValueChange={setDarkMode} trackColor={{ true: Colors.primary }} testID='darkmode-switch' />
          </View>
        </View>
        <TouchableOpacity style={profileStyles.logoutBtn} testID='logout-btn'>
          <Text style={profileStyles.logoutText}>Sign Out</Text>
        </TouchableOpacity>
      </ScrollView>
    </SafeAreaView>
  );
};

const profileStyles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: Colors.background },
  content: { padding: Spacing.lg, alignItems: 'center' },
  avatar: { width: 80, height: 80, borderRadius: 40, backgroundColor: Colors.primary, alignItems: 'center', justifyContent: 'center', marginBottom: Spacing.md },
  avatarText: { ...Typography.h1, color: '#FFF' },
  name: { ...Typography.h2, color: Colors.text },
  app: { ...Typography.body, color: Colors.textSecondary, marginBottom: Spacing.lg },
  statsRow: { flexDirection: 'row', width: '100%', justifyContent: 'space-around', marginBottom: Spacing.lg },
  stat: { alignItems: 'center' },
  statValue: { ...Typography.h3, color: Colors.primary },
  statLabel: { ...Typography.caption, color: Colors.textSecondary },
  section: { width: '100%', marginBottom: Spacing.lg },
  sectionTitle: { ...Typography.h3, color: Colors.text, marginBottom: Spacing.sm },
  row: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', backgroundColor: Colors.card, borderRadius: BorderRadius.md, padding: Spacing.md, marginBottom: Spacing.sm },
  rowLabel: { ...Typography.body, color: Colors.text },
  logoutBtn: { backgroundColor: Colors.error, borderRadius: BorderRadius.lg, paddingVertical: Spacing.md, paddingHorizontal: Spacing.xl, marginTop: Spacing.md },
  logoutText: { ...Typography.body, color: '#FFF', fontWeight: '700' },
});
export default ProfileScreen;
