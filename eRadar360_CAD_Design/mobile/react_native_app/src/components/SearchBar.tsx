import React, { useState } from 'react';
import { View, TextInput, StyleSheet, TouchableOpacity, Text } from 'react-native';
import { Colors, Typography, Spacing, BorderRadius } from '../theme';

interface SearchBarProps { placeholder?: string; onSearch: (q: string) => void; testID?: string; }

export const SearchBar: React.FC<SearchBarProps> = ({ placeholder = 'Search...', onSearch, testID }) => {
  const [query, setQuery] = useState('');
  return (
    <View style={sbStyles.container} testID={testID}>
      <TextInput style={sbStyles.input} value={query} onChangeText={setQuery}
        placeholder={placeholder} placeholderTextColor={Colors.textSecondary}
        returnKeyType='search' onSubmitEditing={() => onSearch(query)}
        testID={testID ? `${testID}-input` : undefined} />
      <TouchableOpacity style={sbStyles.btn} onPress={() => onSearch(query)}
        testID={testID ? `${testID}-btn` : undefined}>
        <Text style={sbStyles.btnText}>Go</Text>
      </TouchableOpacity>
    </View>
  );
};

const sbStyles = StyleSheet.create({
  container: { flexDirection: 'row', alignItems: 'center', marginBottom: Spacing.md },
  input: { flex: 1, backgroundColor: Colors.surface, borderRadius: BorderRadius.lg, paddingHorizontal: Spacing.md, paddingVertical: Spacing.sm, color: Colors.text, ...Typography.body, borderWidth: 1, borderColor: Colors.border, marginRight: Spacing.sm },
  btn: { backgroundColor: Colors.primary, borderRadius: BorderRadius.lg, paddingHorizontal: Spacing.md, paddingVertical: Spacing.sm },
  btnText: { color: '#FFF', fontWeight: '700' },
});

export default SearchBar;
