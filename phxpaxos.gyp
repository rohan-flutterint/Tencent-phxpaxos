{
  'variables': {
    'protobuf_source_dir': 'third_party/protobuf',
    'leveldb_source_dir': 'third_party/leveldb',
    'leveldb_win_dir': '<(DEPTH)/third_party/leveldb_win',
    'glog_source_dir': 'third_party/glog',
    'gtest_source_dir': 'third_party/gtest',
  },
  'targets': [
    {
      'target_name': 'phxpaxos_port',
      'direct_dependent_settings': {
        'include_dirs': ['port'],
      },
      'conditions': [
        ['OS=="win"', {
          'type': 'static_library',
          'direct_dependent_settings': {
            'include_dirs': ['port/win'],
          },
          'sources': [
            'port/win/dirent.h',
            'port/win/dirent.c',
            'port/win/poll.h',
            'port/win/poll.cpp',
            'port/win/pthread.h',
            'port/win/sched.h',
            'port/win/unistd.h',
            'port/win/unistd.c',
            'port/win/arpa/inet.h',
            'port/win/netinet/in.h',
            'port/win/netinet/tcp.h',
            'port/win/sys/epoll.h',
            'port/win/sys/epoll.cpp',
            'port/win/sys/socket.h',
            'port/win/sys/socket.cpp',
            'port/win/sys/time.h',
            'port/win/sys/time.cpp',
            'port/win/sys/un.h',

            'port/port.h',
            'port/port_win.h',
            'port/port_win.cpp',
          ],
        }, {
          'type': 'none',
        }]
      ],
    },
    {
      'target_name': 'libprotobuf',
      'type': 'static_library',
      'dependencies': ['libprotobuf-lite'],
      'export_dependent_settings': ['libprotobuf-lite'],
      'include_dirs': ['<(protobuf_source_dir)/src'],
      'sources': [
        '<(protobuf_source_dir)/src/google/protobuf/any.cc',
        '<(protobuf_source_dir)/src/google/protobuf/any.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/api.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/importer.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/parser.cc',
        '<(protobuf_source_dir)/src/google/protobuf/descriptor.cc',
        '<(protobuf_source_dir)/src/google/protobuf/descriptor.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/descriptor_database.cc',
        '<(protobuf_source_dir)/src/google/protobuf/duration.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/dynamic_message.cc',
        '<(protobuf_source_dir)/src/google/protobuf/empty.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/extension_set_heavy.cc',
        '<(protobuf_source_dir)/src/google/protobuf/field_mask.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/generated_message_reflection.cc',
        '<(protobuf_source_dir)/src/google/protobuf/io/gzip_stream.cc',
        '<(protobuf_source_dir)/src/google/protobuf/io/printer.cc',
        '<(protobuf_source_dir)/src/google/protobuf/io/strtod.cc',
        '<(protobuf_source_dir)/src/google/protobuf/io/tokenizer.cc',
        '<(protobuf_source_dir)/src/google/protobuf/io/zero_copy_stream_impl.cc',
        '<(protobuf_source_dir)/src/google/protobuf/map_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/message.cc',
        '<(protobuf_source_dir)/src/google/protobuf/reflection_ops.cc',
        '<(protobuf_source_dir)/src/google/protobuf/service.cc',
        '<(protobuf_source_dir)/src/google/protobuf/source_context.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/struct.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/mathlimits.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/substitute.cc',
        '<(protobuf_source_dir)/src/google/protobuf/text_format.cc',
        '<(protobuf_source_dir)/src/google/protobuf/timestamp.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/type.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/unknown_field_set.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/field_comparator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/field_mask_util.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/datapiece.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/default_value_objectwriter.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/error_listener.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/field_mask_utility.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/json_escaping.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/json_objectwriter.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/json_stream_parser.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/object_writer.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/proto_writer.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/protostream_objectsource.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/protostream_objectwriter.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/type_info.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/type_info_test_helper.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/internal/utility.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/json_util.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/message_differencer.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/time_util.cc',
        '<(protobuf_source_dir)/src/google/protobuf/util/type_resolver_util.cc',
        '<(protobuf_source_dir)/src/google/protobuf/wire_format.cc',
        '<(protobuf_source_dir)/src/google/protobuf/wrappers.pb.cc'
      ],
    },
    {
      'target_name': 'libprotobuf-lite',
      'type': 'static_library',
      'include_dirs': ['<(protobuf_source_dir)/src'],
      'conditions': [
        ['OS=="win"', {}, {
          'defines': ['HAVE_PTHREAD'],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': ['<(protobuf_source_dir)/src'],
      },
      'sources': [
        '<(protobuf_source_dir)/src/google/protobuf/arena.cc',
        '<(protobuf_source_dir)/src/google/protobuf/arenastring.cc',
        '<(protobuf_source_dir)/src/google/protobuf/extension_set.cc',
        '<(protobuf_source_dir)/src/google/protobuf/generated_message_util.cc',
        '<(protobuf_source_dir)/src/google/protobuf/io/coded_stream.cc',
        '<(protobuf_source_dir)/src/google/protobuf/io/zero_copy_stream.cc',
        '<(protobuf_source_dir)/src/google/protobuf/io/zero_copy_stream_impl_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/message_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/repeated_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/atomicops_internals_x86_gcc.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/atomicops_internals_x86_msvc.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/bytestream.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/common.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/int128.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/once.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/status.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/statusor.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/stringpiece.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/stringprintf.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/structurally_valid.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/strutil.cc',
        '<(protobuf_source_dir)/src/google/protobuf/stubs/time.cc',
        '<(protobuf_source_dir)/src/google/protobuf/wire_format_lite.cc',
      ],
    },
    {
      'target_name': 'libprotoc',
      'type': 'static_library',
      'dependencies': ['libprotobuf'],
      'sources': [
        '<(protobuf_source_dir)/src/google/protobuf/compiler/code_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/command_line_interface.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_enum.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_enum_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_extension.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_file.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_helpers.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_map_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_message.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_message_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_primitive_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_service.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/cpp/cpp_string_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_doc_comment.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_enum.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_enum_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_field_base.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_helpers.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_map_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_message.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_message_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_primitive_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_reflection_class.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_repeated_enum_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_repeated_message_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_repeated_primitive_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_source_generator_base.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/csharp/csharp_wrapper_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_context.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_doc_comment.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_enum.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_enum_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_enum_field_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_enum_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_extension.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_extension_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_file.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_generator_factory.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_helpers.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_lazy_message_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_lazy_message_field_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_map_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_map_field_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_message.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_message_builder.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_message_builder_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_message_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_message_field_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_message_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_name_resolver.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_primitive_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_primitive_field_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_service.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_shared_code_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_string_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/java/java_string_field_lite.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_enum.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_enum_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_extension.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_file.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_helpers.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_map_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_message.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_message_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/javanano/javanano_primitive_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/js/js_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_enum.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_enum_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_extension.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_file.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_helpers.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_map_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_message.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_message_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_oneof.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/objectivec/objectivec_primitive_field.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/plugin.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/plugin.pb.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/python/python_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/ruby/ruby_generator.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/subprocess.cc',
        '<(protobuf_source_dir)/src/google/protobuf/compiler/zip_writer.cc',
      ],
    },
    {
      'target_name': 'protoc',
      'type': 'executable',
      'dependencies': [
        'libprotoc',
        'libprotobuf',
      ],
      'sources': [
        '<(protobuf_source_dir)/src/google/protobuf/compiler/main.cc',
      ],
    },
    {
      'target_name': 'leveldb',
      'type': 'static_library',
      'conditions': [
        ['OS=="win"', {
          'defines': ['LEVELDB_PLATFORM_WIN'],
          'include_dirs': ['<(leveldb_win_dir)'],
          'sources': [
            '<(leveldb_win_dir)/port/port_win.cc',
            '<(leveldb_win_dir)/port/port_win.h',
            '<(leveldb_win_dir)/util/env_win.cc',
            '<(leveldb_win_dir)/util/win_logger.h',
            '<(leveldb_win_dir)/util/win_logger.cc',
          ],
        }, {
          'defines': [
            'OS_LINUX',
            'LEVELDB_PLATFORM_POSIX'
          ],
          'sources': [
            '<(leveldb_source_dir)/util/env_posix.cc',
            '<(leveldb_source_dir)/port/port_posix.h',
            '<(leveldb_source_dir)/port/port_posix.cc',
            '<(leveldb_source_dir)/util/posix_logger.h',
          ],
        }],
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(leveldb_source_dir)',
          '<(leveldb_source_dir)/include',
        ],
      },
      'include_dirs': [
        '<(leveldb_source_dir)',
        '<(leveldb_source_dir)/include',
      ],
      'sources': [
        '<(leveldb_source_dir)/db/filename.cc',
        '<(leveldb_source_dir)/db/version_edit.cc',
        '<(leveldb_source_dir)/db/repair.cc',
        '<(leveldb_source_dir)/db/log_writer.cc',
        '<(leveldb_source_dir)/db/log_reader.cc',
        '<(leveldb_source_dir)/db/table_cache.cc',
        '<(leveldb_source_dir)/db/memtable.cc',
        '<(leveldb_source_dir)/db/write_batch.cc',
        '<(leveldb_source_dir)/db/builder.cc',
        '<(leveldb_source_dir)/db/db_iter.cc',
        '<(leveldb_source_dir)/db/db_impl.cc',
        '<(leveldb_source_dir)/db/dumpfile.cc',
        '<(leveldb_source_dir)/db/version_set.cc',
        '<(leveldb_source_dir)/db/dbformat.cc',
        '<(leveldb_source_dir)/util/options.cc',
        '<(leveldb_source_dir)/util/histogram.cc',
        '<(leveldb_source_dir)/util/cache.cc',
        '<(leveldb_source_dir)/util/hash.cc',
        '<(leveldb_source_dir)/util/comparator.cc',
        '<(leveldb_source_dir)/util/arena.cc',
        '<(leveldb_source_dir)/util/env.cc',
        '<(leveldb_source_dir)/util/logging.cc',
        '<(leveldb_source_dir)/util/crc32c.cc',
        '<(leveldb_source_dir)/util/status.cc',
        '<(leveldb_source_dir)/util/filter_policy.cc',
        '<(leveldb_source_dir)/util/coding.cc',
        '<(leveldb_source_dir)/util/bloom.cc',
        '<(leveldb_source_dir)/table/table_builder.cc',
        '<(leveldb_source_dir)/table/merger.cc',
        '<(leveldb_source_dir)/table/block_builder.cc',
        '<(leveldb_source_dir)/table/two_level_iterator.cc',
        '<(leveldb_source_dir)/table/block.cc',
        '<(leveldb_source_dir)/table/filter_block.cc',
        '<(leveldb_source_dir)/table/table.cc',
        '<(leveldb_source_dir)/table/format.cc',
        '<(leveldb_source_dir)/table/iterator.cc',
      ],
    },
    {
      'target_name': 'glog',
      'type': 'static_library',
      'defines': ['GOOGLE_GLOG_DLL_DECL='],
      'direct_dependent_settings': {
        'defines': ['GOOGLE_GLOG_DLL_DECL='],
      },
      'include_dirs': [
        '<(glog_source_dir)/src'
      ],
      'conditions': [
        ['OS=="win"', {
          'sources': [
            '<(glog_source_dir)/src/windows/glog/log_severity.h',
            '<(glog_source_dir)/src/windows/glog/logging.h',
            '<(glog_source_dir)/src/windows/glog/raw_logging.h',
            '<(glog_source_dir)/src/windows/glog/vlog_is_on.h',
            '<(glog_source_dir)/src/windows/glog/stl_logging.h',

            '<(glog_source_dir)/src/windows/config.h',
            '<(glog_source_dir)/src/windows/port.cc',
            '<(glog_source_dir)/src/windows/port.h',
          ],
          'include_dirs': ['<(glog_source_dir)/src/windows'],
          'direct_dependent_settings': {
            'include_dirs': [
              '<(glog_source_dir)/src/windows'
            ],
          },
        }, {
          'sources': [
            '<(glog_source_dir)/src/glog/log_severity.h',
            '<(glog_source_dir)/src/glog/logging.h',
            '<(glog_source_dir)/src/glog/raw_logging.h',
            '<(glog_source_dir)/src/glog/vlog_is_on.h',
            '<(glog_source_dir)/src/glog/stl_logging.h',
            '<(glog_source_dir)/src/signalhandler.cc',
          ],
          'direct_dependent_settings': {
            'include_dirs': [
              '<(glog_source_dir)/src'
            ],
          },
        }],
      ],
      'sources': [
        '<(glog_source_dir)/src/logging.cc',
        '<(glog_source_dir)/src/raw_logging.cc',
        '<(glog_source_dir)/src/vlog_is_on.cc',
        '<(glog_source_dir)/src/utilities.cc',
        '<(glog_source_dir)/src/utilities.h',
        '<(glog_source_dir)/src/demangle.cc',
        '<(glog_source_dir)/src/demangle.h',
        '<(glog_source_dir)/src/stacktrace.h',
        '<(glog_source_dir)/src/stacktrace_generic-inl.h',
        '<(glog_source_dir)/src/stacktrace_libunwind-inl.h',
        '<(glog_source_dir)/src/stacktrace_powerpc-inl.h',
        '<(glog_source_dir)/src/stacktrace_x86-inl.h',
        '<(glog_source_dir)/src/stacktrace_x86_64-inl.h',
        '<(glog_source_dir)/src/symbolize.cc',
        '<(glog_source_dir)/src/symbolize.h',
        '<(glog_source_dir)/src/base/mutex.h',
        '<(glog_source_dir)/src/base/googleinit.h',
        '<(glog_source_dir)/src/base/commandlineflags.h',
        '<(glog_source_dir)/src/googletest.h',
      ],
    },
    {
      'target_name': 'gtest',
      'type': 'static_library',
      'include_dirs': [
        '<(gtest_source_dir)/googletest/include',
        '<(gtest_source_dir)/googlemock/include',
        '<(gtest_source_dir)/googletest',
        '<(gtest_source_dir)/googlemock',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(gtest_source_dir)/googletest/include',
          '<(gtest_source_dir)/googlemock/include'
        ],
      },
      'sources': [
        '<(gtest_source_dir)/googletest/src/gtest-all.cc',
        '<(gtest_source_dir)/googlemock/src/gmock-all.cc',
      ],
    },
    {
      'target_name': 'phxpaxos',
      'type': 'static_library',
      'dependencies': [
        'leveldb',
        'libprotobuf',
        'phxpaxos_port',
      ],
      'conditions': [
        ['OS=="win"', {
          'sources': ['src/communicate/tcp/notify_win.cpp'],
          'direct_dependent_settings': {
            'libraries': ['-lws2_32.lib'],
          }
        }, {
          'sources': ['src/communicate/tcp/notify.cpp'],
        }]
      ],
      'export_dependent_settings': [
        'leveldb',
        'libprotobuf',
        'phxpaxos_port',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'include',
          'src',
        ],
      },
      'include_dirs': [
        'include',
        'src',

        'src/utils',
        'src/algorithm',
        'src/checkpoint',
        'src/comm',
        'src/communicate',
        'src/communicate/tcp',
        'src/config',
        'src/logstorage',
        'src/master',
        'src/node',
        'src/sm-base',
        'src/tools',
      ],
      'sources': [
        'include/phxpaxos/breakpoint.h',
        'include/phxpaxos/def.h',
        'include/phxpaxos/log.h',
        'include/phxpaxos/network.h',
        'include/phxpaxos/node.h',
        'include/phxpaxos/options.h',
        'include/phxpaxos/sm.h',
        'include/phxpaxos/storage.h',

        'src/algorithm/acceptor.cpp',
        'src/algorithm/acceptor.h',
        'src/algorithm/base.cpp',
        'src/algorithm/base.h',
        'src/algorithm/checkpoint_receiver.cpp',
        'src/algorithm/checkpoint_receiver.h',
        'src/algorithm/checkpoint_sender.cpp',
        'src/algorithm/checkpoint_sender.h',
        'src/algorithm/commitctx.cpp',
        'src/algorithm/commitctx.h',
        'src/algorithm/committer.cpp',
        'src/algorithm/committer.h',
        'src/algorithm/instance.cpp',
        'src/algorithm/instance.h',
        'src/algorithm/ioloop.cpp',
        'src/algorithm/ioloop.h',
        'src/algorithm/learner.cpp',
        'src/algorithm/learner.h',
        'src/algorithm/learner_sender.cpp',
        'src/algorithm/learner_sender.h',
        'src/algorithm/msg_counter.cpp',
        'src/algorithm/msg_counter.h',
        'src/algorithm/proposer.cpp',
        'src/algorithm/proposer.h',
        'src/checkpoint/cleaner.cpp',
        'src/checkpoint/cleaner.h',
        'src/checkpoint/cp_mgr.cpp',
        'src/checkpoint/cp_mgr.h',
        'src/checkpoint/replayer.cpp',
        'src/checkpoint/replayer.h',
        'src/comm/breakpoint.cpp',
        'src/comm/commdef.h',
        'src/comm/comm_include.h',
        'src/comm/inside_options.cpp',
        'src/comm/inside_options.h',
        'src/comm/logger.cpp',
        'src/comm/logger.h',
        'src/comm/msg_transport.h',
        'src/comm/options.cpp',
        'src/comm/paxos_msg.proto',

        'src/communicate/communicate.cpp',
        'src/communicate/communicate.h',
        'src/communicate/dfnetwork.cpp',
        'src/communicate/dfnetwork.h',
        'src/communicate/network.cpp',
        'src/communicate/tcp/event_base.cpp',
        'src/communicate/tcp/event_base.h',
        'src/communicate/tcp/event_loop.cpp',
        'src/communicate/tcp/event_loop.h',
        'src/communicate/tcp/message_event.cpp',
        'src/communicate/tcp/message_event.h',
        'src/communicate/tcp/notify.h',
        'src/communicate/tcp/tcp.cpp',
        'src/communicate/tcp/tcp.h',
        'src/communicate/tcp/tcp_acceptor.cpp',
        'src/communicate/tcp/tcp_acceptor.h',
        'src/communicate/tcp/tcp_client.cpp',
        'src/communicate/tcp/tcp_client.h',
        'src/communicate/udp.cpp',
        'src/communicate/udp.h',
        'src/config/config.cpp',
        'src/config/config.h',
        'src/config/config_include.h',
        'src/config/inside_sm.h',
        'src/config/system_v_sm.cpp',
        'src/config/system_v_sm.h',
        'src/logstorage/db.cpp',
        'src/logstorage/db.h',
        'src/logstorage/log_store.cpp',
        'src/logstorage/log_store.h',
        'src/logstorage/paxos_log.cpp',
        'src/logstorage/paxos_log.h',
        'src/logstorage/system_variables_store.cpp',
        'src/logstorage/system_variables_store.h',
        'src/master/master_mgr.cpp',
        'src/master/master_mgr.h',
        'src/master/master_sm.cpp',
        'src/master/master_sm.h',
        'src/master/master_sm.proto',
        'src/master/master_variables_store.cpp',
        'src/master/master_variables_store.h',
        'src/node/group.cpp',
        'src/node/group.h',
        'src/node/node.cpp',
        'src/node/pnode.cpp',
        'src/node/pnode.h',
        'src/node/propose_batch.cpp',
        'src/node/propose_batch.h',
        'src/sm-base/sm.cpp',
        'src/sm-base/sm_base.cpp',
        'src/sm-base/sm_base.h',

        'src/utils/bytes_buffer.cpp',
        'src/utils/bytes_buffer.h',
        'src/utils/concurrent.cpp',
        'src/utils/concurrent.h',
        'src/utils/crc32.cpp',
        'src/utils/crc32.h',
        'src/utils/notifier_pool.cpp',
        'src/utils/notifier_pool.h',
        'src/utils/serial_lock.cpp',
        'src/utils/serial_lock.h',
        'src/utils/socket.cpp',
        'src/utils/socket.h',
        'src/utils/timer.cpp',
        'src/utils/timer.h',
        'src/utils/util.cpp',
        'src/utils/util.h',
        'src/utils/utils_include.h',
        'src/utils/wait_lock.cpp',
        'src/utils/wait_lock.h',
      ],
      'includes': ['protoc.gypi'],
    },
    {
      'target_name': 'phxpaxos_plugin',
      'type': 'static_library',
      'dependencies': [
        'glog',
        'phxpaxos',
      ],
      'export_dependent_settings': [
        'glog',
        'phxpaxos',
      ],
      'include_dirs': ['plugin/include'],
      'direct_dependent_settings': {
        'include_dirs': ['plugin/include'],
      },
      'sources': [
        'plugin/include/phxpaxos_plugin/logger_google.h',
        'plugin/include/phxpaxos_plugin/monitor.h',
        'plugin/logger_google/logger_google.cpp',
        'plugin/logger_google/logger_google_impl.cpp',
        'plugin/logger_google/logger_google_impl.h',
        'plugin/monitor/monitor.cpp',
        'plugin/monitor/monitor_bp.cpp',
        'plugin/monitor/monitor_bp.h',
      ],
    },
    {
      'target_name': 'phxecho',
      'type': 'executable',
      'dependencies': ['phxpaxos', 'phxpaxos_plugin'],
      'sources': [
        'sample/phxecho/echo_server.cpp',
        'sample/phxecho/echo_server.h',
        'sample/phxecho/echo_sm.cpp',
        'sample/phxecho/echo_sm.h',
        'sample/phxecho/main.cpp',
      ],
    },
    {
      'target_name': 'phxelection',
      'type': 'executable',
      'dependencies': ['phxpaxos', 'phxpaxos_plugin'],
      'sources': [
        'sample/phxelection/election.cpp',
        'sample/phxelection/election.h',
        'sample/phxelection/election_main.cpp',
      ],
    },
    {
      'target_name': 'phxpaxos_ut',
      'type': 'executable',
      'dependencies': [
        'phxpaxos',
        'gtest',
      ],
      'include_dirs': [
        'src/utils',
        'src/algorithm',
        'src/checkpoint',
        'src/comm',
        'src/communicate',
        'src/communicate/tcp',
        'src/config',
        'src/logstorage',
        'src/master',
        'src/node',
        'src/sm-base',
        'src/tools',
      ],
      'sources': [
        'src/ut/acceptor_ut.cpp',
        'src/ut/db_ut.cpp',
        'src/ut/make_class.cpp',
        'src/ut/make_class.h',
        'src/ut/mock_class.h',
        'src/ut/nodeid_ut.cpp',
        'src/ut/proposer_ut.cpp',
        'src/ut/timer_ut.cpp',
        'src/ut/ut_main.cpp',
        'src/ut/wait_lock_ut.cpp',
      ],
    },
  ]
}