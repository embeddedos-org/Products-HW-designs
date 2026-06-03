import 'package:flutter/material.dart';
import '../../core/theme/app_theme.dart';
import '../../core/widgets/common_widgets.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});
  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  bool _notifications = true;
  bool _darkMode = false;
  bool _locationServices = true;
  String _language = 'English';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Settings')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          _SectionLabel('Preferences'),
          AppCard(
            child: Column(
              children: [
                _ToggleTile('Push Notifications', Icons.notifications_outlined,
                  _notifications, (v) => setState(() => _notifications = v)),
                const Divider(height: 1),
                _ToggleTile('Dark Mode', Icons.dark_mode_outlined,
                  _darkMode, (v) => setState(() => _darkMode = v)),
                const Divider(height: 1),
                _ToggleTile('Location Services', Icons.location_on_outlined,
                  _locationServices, (v) => setState(() => _locationServices = v)),
              ],
            ),
          ),
          const SizedBox(height: 16),
          _SectionLabel('Account'),
          AppCard(
            child: Column(
              children: [
                _NavTile('Language', Icons.language_outlined, _language, () {}),
                const Divider(height: 1),
                _NavTile('Privacy Policy', Icons.privacy_tip_outlined, '', () {}),
                const Divider(height: 1),
                _NavTile('Terms of Service', Icons.description_outlined, '', () {}),
                const Divider(height: 1),
                _NavTile('About eRadar360', Icons.info_outlined, 'v1.0.0', () {}),
              ],
            ),
          ),
          const SizedBox(height: 16),
          _SectionLabel('Danger Zone'),
          AppCard(
            child: _NavTile('Delete Account', Icons.delete_outline,
              '', () {}, color: AppTheme.error),
          ),
        ],
      ),
    );
  }
}

class _SectionLabel extends StatelessWidget {
  final String label;
  const _SectionLabel(this.label);
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8, left: 4),
      child: Text(label.toUpperCase(),
        style: const TextStyle(
          fontSize: 11, fontWeight: FontWeight.w700,
          color: AppTheme.textSecondary, letterSpacing: 1.2)),
    );
  }
}

class _ToggleTile extends StatelessWidget {
  final String label;
  final IconData icon;
  final bool value;
  final ValueChanged<bool> onChanged;
  const _ToggleTile(this.label, this.icon, this.value, this.onChanged);
  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: Icon(icon, color: AppTheme.primary, size: 22),
      title: Text(label, style: const TextStyle(fontWeight: FontWeight.w500)),
      trailing: Switch(value: value, onChanged: onChanged, activeColor: AppTheme.primary),
      contentPadding: const EdgeInsets.symmetric(horizontal: 4),
    );
  }
}

class _NavTile extends StatelessWidget {
  final String label, subtitle;
  final IconData icon;
  final VoidCallback onTap;
  final Color? color;
  const _NavTile(this.label, this.icon, this.subtitle, this.onTap, {this.color});
  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: Icon(icon, color: color ?? AppTheme.primary, size: 22),
      title: Text(label,
        style: TextStyle(fontWeight: FontWeight.w500, color: color ?? AppTheme.textPrimary)),
      trailing: subtitle.isNotEmpty
        ? Text(subtitle, style: const TextStyle(color: AppTheme.textSecondary, fontSize: 13))
        : const Icon(Icons.chevron_right, color: AppTheme.textSecondary),
      onTap: onTap,
      contentPadding: const EdgeInsets.symmetric(horizontal: 4),
    );
  }
}
