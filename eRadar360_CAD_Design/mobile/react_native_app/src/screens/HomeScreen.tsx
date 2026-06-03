import React, { useEffect, useState } from 'react';
import { View, Text, StyleSheet, ScrollView, ActivityIndicator, RefreshControl, StatusBar } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Colors, Typography, Spacing, BorderRadius } from '../theme';
import { Card } from '../components/Card';

interface FeaturedItem { id: string; title: string; subtitle: string; badge?: string; }

const FEATURED: FeaturedItem[] = [
  { id: '1', title: 'Get Started with eRadar360_CAD', subtitle: '360-degree driver awareness radar', badge: 'NEW' },
  { id: '2', title: 'Quick Actions', subtitle: 'Access your most-used features', badge: 'HOT' },
  { id: '3', title: 'Recent Activity', subtitle: 'Pick up where you left off' },
];

export const HomeScreen: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [items, setItems] = useState<FeaturedItem[]>([]);

  const loadData = async () => { await new Promise(r => setTimeout(r, 300)); setItems(FEATURED); setLoading(false); };
  useEffect(() => { loadData(); }, []);
  const onRefresh = async () => { setRefreshing(true); await loadData(); setRefreshing(false); };

  return (
    <SafeAreaView style={homeStyles.safe} testID='home-screen'>
      <StatusBar barStyle='light-content' backgroundColor={Colors.primary} />
      <View style={homeStyles.header}>
        <Text style={homeStyles.appName} testID='app-name'>eRadar360_CAD</Text>
        <Text style={homeStyles.tagline}>360-degree driver awareness radar</Text>
      </View>
      {loading ? (
        <View style={homeStyles.center} testID='loading-indicator'>
          <ActivityIndicator size='large' color={Colors.primary} />
        </View>
      ) : (
        <ScrollView style={homeStyles.scroll} contentContainerStyle={homeStyles.content}
          refreshControl={<RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={Colors.primary} />}
          testID='home-scroll'>
          <Text style={homeStyles.sectionTitle}>Featured</Text>
          {items.map(item => (
            <Card key={item.id} title={item.title} subtitle={item.subtitle} badge={item.badge} onPress={() => {}} testID={'card-' + item.id} />
          ))}
          <View style={homeStyles.statsRow}>
            {['iOS', 'Android', 'Web'].map(p => (
              <View key={p} style={homeStyles.statBox} testID={'platform-' + p.toLowerCase()}>
                <Text style={homeStyles.statValue}>✓</Text>
                <Text style={homeStyles.statLabel}>{p}</Text>
              </View>
            ))}
          </View>
        </ScrollView>
      )}
    </SafeAreaView>
  );
};

const homeStyles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: Colors.background },
  header: { backgroundColor: Colors.primary, paddingHorizontal: Spacing.lg, paddingVertical: Spacing.lg },
  appName: { ...Typography.h1, color: '#FFFFFF' },
  tagline: { ...Typography.body, color: 'rgba(255,255,255,0.8)', marginTop: 4 },
  scroll: { flex: 1 },
  content: { padding: Spacing.md },
  center: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  sectionTitle: { ...Typography.h3, color: Colors.text, marginBottom: Spacing.sm },
  statsRow: { flexDirection: 'row', justifyContent: 'space-around', marginTop: Spacing.lg },
  statBox: { alignItems: 'center', backgroundColor: Colors.card, borderRadius: BorderRadius.md, padding: Spacing.md, flex: 1, marginHorizontal: 4 },
  statValue: { ...Typography.h2, color: Colors.primary },
  statLabel: { ...Typography.caption, color: Colors.textSecondary, marginTop: 4 },
});
export default HomeScreen;
