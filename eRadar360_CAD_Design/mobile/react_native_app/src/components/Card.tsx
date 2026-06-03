import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ViewStyle } from 'react-native';
import { Colors, Typography, Spacing, BorderRadius } from '../theme';

interface CardProps {
  title: string;
  subtitle?: string;
  badge?: string;
  onPress?: () => void;
  style?: ViewStyle;
  testID?: string;
}

export const Card: React.FC<CardProps> = ({ title, subtitle, badge, onPress, style, testID }) => {
  const Container: any = onPress ? TouchableOpacity : View;
  return (
    <Container style={[cardStyles.card, style]} onPress={onPress} testID={testID} activeOpacity={0.8}>
      <View style={cardStyles.content}>
        <Text style={cardStyles.title} numberOfLines={2}>{title}</Text>
        {subtitle ? <Text style={cardStyles.subtitle} numberOfLines={1}>{subtitle}</Text> : null}
      </View>
      {badge ? (
        <View style={cardStyles.badge}>
          <Text style={cardStyles.badgeText}>{badge}</Text>
        </View>
      ) : null}
    </Container>
  );
};

const cardStyles = StyleSheet.create({
  card: { backgroundColor: Colors.card, borderRadius: BorderRadius.lg, padding: Spacing.md, marginBottom: Spacing.sm, borderWidth: 1, borderColor: Colors.border, flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' },
  content: { flex: 1, marginRight: Spacing.sm },
  title: { ...Typography.body, color: Colors.text, fontWeight: '600' },
  subtitle: { ...Typography.caption, color: Colors.textSecondary, marginTop: 2 },
  badge: { backgroundColor: Colors.primary, borderRadius: BorderRadius.full, paddingHorizontal: Spacing.sm, paddingVertical: 2 },
  badgeText: { ...Typography.caption, color: '#FFFFFF', fontWeight: '700' },
});

export default Card;
