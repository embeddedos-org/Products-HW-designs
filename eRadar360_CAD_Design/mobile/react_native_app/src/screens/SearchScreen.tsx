import React, { useState } from 'react';
import { View, Text, StyleSheet, FlatList, TouchableOpacity } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Colors, Typography, Spacing, BorderRadius } from '../theme';
import { SearchBar } from '../components/SearchBar';
import { Card } from '../components/Card';

const FILTERS = ['All', 'Popular', 'New', 'Nearby', 'Top Rated'];

export const SearchScreen: React.FC = () => {
  const [query, setQuery] = useState('');
  const [activeFilter, setActiveFilter] = useState('All');
  const [results, setResults] = useState<{id:string;title:string;subtitle:string}[]>([]);

  const handleSearch = (q: string) => {
    setQuery(q);
    if (q.trim()) {
      setResults([
        { id: '1', title: q + ' — Result 1', subtitle: '360-degree driver awareness radar' },
        { id: '2', title: q + ' — Result 2', subtitle: 'Tap to view details' },
      ]);
    } else { setResults([]); }
  };

  return (
    <SafeAreaView style={searchStyles.safe} testID='search-screen'>
      <View style={searchStyles.container}>
        <Text style={searchStyles.title}>Search</Text>
        <SearchBar placeholder='Search...' onSearch={handleSearch} testID='main-search' />
        <View style={searchStyles.filters} testID='filter-row'>
          {FILTERS.map(f => (
            <TouchableOpacity key={f} style={[searchStyles.chip, activeFilter === f && searchStyles.chipActive]}
              onPress={() => setActiveFilter(f)} testID={'filter-' + f.toLowerCase()}>
              <Text style={[searchStyles.chipText, activeFilter === f && searchStyles.chipTextActive]}>{f}</Text>
            </TouchableOpacity>
          ))}
        </View>
        {results.length === 0 ? (
          <View style={searchStyles.empty} testID='empty-state'>
            <Text style={searchStyles.emptyText}>{query ? 'No results found' : 'Start searching...'}</Text>
          </View>
        ) : (
          <FlatList data={results} keyExtractor={i => i.id}
            renderItem={({ item }) => <Card title={item.title} subtitle={item.subtitle} testID={'result-' + item.id} />}
            testID='results-list' />
        )}
      </View>
    </SafeAreaView>
  );
};

const searchStyles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: Colors.background },
  container: { flex: 1, padding: Spacing.md },
  title: { ...Typography.h2, color: Colors.text, marginBottom: Spacing.md },
  filters: { flexDirection: 'row', flexWrap: 'wrap', marginBottom: Spacing.md },
  chip: { backgroundColor: Colors.surface, borderRadius: BorderRadius.full, paddingHorizontal: Spacing.md, paddingVertical: Spacing.xs, marginRight: Spacing.xs, marginBottom: Spacing.xs, borderWidth: 1, borderColor: Colors.border },
  chipActive: { backgroundColor: Colors.primary, borderColor: Colors.primary },
  chipText: { ...Typography.label, color: Colors.textSecondary },
  chipTextActive: { color: '#FFFFFF' },
  empty: { flex: 1, alignItems: 'center', justifyContent: 'center' },
  emptyText: { ...Typography.body, color: Colors.textSecondary },
});
export default SearchScreen;
